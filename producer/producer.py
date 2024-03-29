from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pysnmp.smi import builder, view, compiler, rfc1902
import json
from datetime import datetime, timedelta
from confluent_kafka import Producer
import logging
import random
import re

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p = Producer({'bootstrap.servers':'kafka1:19091'})
print('Kafka Producer has been initiated...')

def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    print('cbFun is called')
    global minute
    while wholeMsg:
        print('loop...')
        # print(wholeMsg)
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        print('Version: %s' % (msgVer))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(wholeMsg, asn1Spec=pMod.Message(),)
        print('Notification message from %s:%s: ' % (transportDomain, transportAddress))
        trapInfo = []
        trapInfo.append(transportAddress[0])
        print('ReqMsg: %s' % (reqMsg))
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        print('ReqPDU: %s' % (reqPDU))
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                trapInfo.append("1")
                enterprise = pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                print('Enterprise: %s' % (enterprise))
                agentAdress = pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                print('Agent Address: %s' % (agentAdress))
                genericTrap = pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                print('Generic Trap: %s' % (genericTrap))
                specificTrap = pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                print('Specific Trap: %s' % (specificTrap))
                uptime = pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                print('Uptime: %s' % (uptime))

                if genericTrap == "coldStart" or genericTrap == "warmStart":
                    trapInfo.append("SNMPv2-MIB")
                else:
                    trapInfo.append("IF-MIB")

                trapInfo.append(genericTrap)

                trapInfo.append([])
                
                dateTime = datetime.now()+ timedelta(minutes=minute)
                dateTimeStr = dateTime.strftime('%Y-%m-%d %H:%M:%S')
                trapInfo.append(dateTimeStr)
                minute = minute+random.randint(5, 45)
                jsonTrap = {}
                nombresClaves = ["IPSource", "Version", "MIB", "Type", "AdditionalInfo", "Datetime"]
                for i in range(len(trapInfo)):
                    jsonTrap[nombresClaves[i]] = trapInfo[i]

                jsonStr = json.dumps(jsonTrap, indent=5)
                jsonTrap = json.loads(jsonStr)
                m=json.dumps(jsonTrap)
                p.poll(1)
                # Producimos en el topic snmptrap-tracker
                p.produce('snmptrap-tracker', m.encode('utf-8'),callback=receipt)
                p.flush()
            else:
                trapInfo.append("2")
                mibBuilder = builder.MibBuilder()

                # SI NO FUNCIONA DESCOMENTAR. AQUI SE VE LA RUTA QUE COGE LOS MIBs
                # pysmi_debug.setLogger(pysmi_debug.Debug('compiler'))

                compiler.addMibCompiler(mibBuilder)
                mibViewController = view.MibViewController(mibBuilder)

                # Pre-load MIB modules we expect to work with
                mibBuilder.loadModules('IF-MIB')
                print("TRADUCCION2.............")
                # ent = rfc1902.ObjectType(rfc1902.ObjectIdentity(enterprise)).resolveWithMib(mibViewController)
                # print(ent)
                resolvedVarBinds = []
                varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
                cont=0
                for oid, val in varBinds:
                    resolvedVarBind = rfc1902.ObjectType(rfc1902.ObjectIdentity(oid), val).resolveWithMib(mibViewController)
                    if cont==0:
                        coldStart = r"SNMPv2-MIB::coldStart"
                        warmStart = r"SNMPv2-MIB::warmStart"
                        linkDown = r"IF-MIB::linkDown"
                        linkUp = r"IF-MIB::linkUp"
                        authenticationFailure = r"SNMPv2-MIB::authenticationFailure"
                        if re.search(coldStart, resolvedVarBind.prettyPrint()):
                            trapInfo.append("SNMPv2-MIB")
                            trapInfo.append("coldStart")
                            print(resolvedVarBind)
                        elif re.search(warmStart, resolvedVarBind.prettyPrint()):
                            trapInfo.append("SNMPv2-MIB")
                            trapInfo.append("warmStart")
                            print(resolvedVarBind)
                        elif re.search(linkDown, resolvedVarBind.prettyPrint()):
                            trapInfo.append("IF-MIB")
                            trapInfo.append("linkDown")
                            print(resolvedVarBind)
                        elif re.search(linkUp, resolvedVarBind.prettyPrint()):
                            trapInfo.append("IF-MIB")
                            trapInfo.append("linkUp")
                            print(resolvedVarBind)
                        elif re.search(authenticationFailure, resolvedVarBind.prettyPrint()):
                            trapInfo.append("IF-MIB")
                            trapInfo.append("authenticationFailure")
                            print(resolvedVarBind)
                    else:
                        resolvedVarBinds.append(resolvedVarBind.prettyPrint())
                        print(resolvedVarBind)
                    cont = cont+1
                trapInfo.append(resolvedVarBinds)
                dateTime = datetime.now()+ timedelta(minutes=minute)
                dateTimeStr = dateTime.strftime('%Y-%m-%d %H:%M:%S')
                trapInfo.append(dateTimeStr)
                minute = minute+random.randint(5, 45)
                jsonTrap = {}
                nombresClaves = ["IPSource", "Version", "MIB", "Type", "AdditionalInfo", "Datetime"]
                for i in range(len(trapInfo)):
                    jsonTrap[nombresClaves[i]] = trapInfo[i]

                jsonStr = json.dumps(jsonTrap, indent=5)
                jsonTrap = json.loads(jsonStr)
                m=json.dumps(jsonTrap)
                p.poll(1)
                # Producimos en el topic snmptrap-tracker
                p.produce('snmptrap-tracker', m.encode('utf-8'),callback=receipt)
                p.flush()
    return wholeMsg

minute = 0

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

# while True:
transportDispatcher = AsynsockDispatcher()

transportDispatcher.registerRecvCbFun(cbFun)
# UDP/IPv4
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
)

# # UDP/IPv6
# transportDispatcher.registerTransport(
#     udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 163))
# )

transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    print('run dispatcher')
    transportDispatcher.runDispatcher()
except:
    transportDispatcher.closeDispatcher()
    raise    