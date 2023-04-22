import subprocess
import time

# Simulacion de una caida y restauracion recurrente de una interfaz
def pipeline1():
    time.sleep(4)
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    time.sleep(1)
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    
# Simula un posible ataque en la red
def pipeline2():
    time.sleep(4)
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    time.sleep(1)
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB:: authenticationFailure"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])    

# Simula una caida de todas las interfaces vituales de un dispositivo
def pipeline3():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"vlan1"',"IF-MIB::ifType.1","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"vlan2"',"IF-MIB::ifType.2","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.3", "i", "3",
                    "IF-MIB::ifDescr.3","s",'"vlan3"',"IF-MIB::ifType.3","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.4", "i", "4",
                    "IF-MIB::ifDescr.4","s",'"vlan4"',"IF-MIB::ifType.4","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.5", "i", "5",
                    "IF-MIB::ifDescr.5","s",'"vlan5"',"IF-MIB::ifType.5","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.6", "i", "6",
                    "IF-MIB::ifDescr.6","s",'"vlan6"',"IF-MIB::ifType.6","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.7", "i", "7",
                    "IF-MIB::ifDescr.7","s",'"vlan7"',"IF-MIB::ifType.7","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.8", "i", "8",
                    "IF-MIB::ifDescr.8","s",'"vlan8"',"IF-MIB::ifType.8","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.9", "i", "9",
                    "IF-MIB::ifDescr.9","s",'"vlan9"',"IF-MIB::ifType.9","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.10", "i", "10",
                    "IF-MIB::ifDescr.10","s",'"vlan10"',"IF-MIB::ifType.10","i","7"])

def main():
    pipeline3()
    print("SALIDA")

main()