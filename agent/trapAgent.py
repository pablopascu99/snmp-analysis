import subprocess

def pipeline0():
    # subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
    #                 "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    # subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
    #                 "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
# Simulacion de una caida y restauracion recurrente de una interfaz
def pipeline1():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    
# Simula un posible ataque de autenticacion en la red
def pipeline2():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])    
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"]) 
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 5'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","6"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"eth0"',"IF-MIB::ifType.1","i","6"]) 

# Simula una caida de todas las interfaces virtuales de un dispositivo y reestablecimiento posterior
def pipeline3():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"vlan1"',"IF-MIB::ifType.1","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.1", "i", "1",
                     "ifDescr.1","s",'"vlan1"',"ifType.1","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"vlan2"',"IF-MIB::ifType.2","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.2","s",'"vlan2"',"ifType.2","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.3", "i", "3",
                    "IF-MIB::ifDescr.3","s",'"vlan3"',"IF-MIB::ifType.3","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.3", "i", "3",
                     "ifDescr.3","s",'"vlan3"',"ifType.3","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.4", "i", "4",
                    "IF-MIB::ifDescr.4","s",'"vlan4"',"IF-MIB::ifType.4","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.4", "i", "4",
                     "ifDescr.4","s",'"vlan4"',"ifType.4","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.5", "i", "5",
                    "IF-MIB::ifDescr.5","s",'"vlan5"',"IF-MIB::ifType.5","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.5", "i", "5",
                     "ifDescr.5","s",'"vlan5"',"ifType.5","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.6", "i", "6",
                    "IF-MIB::ifDescr.6","s",'"vlan6"',"IF-MIB::ifType.6","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.6", "i", "6",
                     "ifDescr.6","s",'"vlan6"',"ifType.6","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.7", "i", "7",
                    "IF-MIB::ifDescr.7","s",'"vlan7"',"IF-MIB::ifType.7","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.7", "i", "7",
                     "ifDescr.7","s",'"vlan7"',"ifType.7","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.8", "i", "8",
                    "IF-MIB::ifDescr.8","s",'"vlan8"',"IF-MIB::ifType.8","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.8", "i", "8",
                     "ifDescr.8","s",'"vlan8"',"ifType.8","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.9", "i", "9",
                    "IF-MIB::ifDescr.9","s",'"vlan9"',"IF-MIB::ifType.9","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.9", "i", "9",
                     "ifDescr.9","s",'"vlan9"',"ifType.9","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.10", "i", "10",
                    "IF-MIB::ifDescr.10","s",'"vlan10"',"IF-MIB::ifType.10","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.10", "i", "10",
                     "ifDescr.10","s",'"vlan10"',"ifType.10","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.1", "i", "1",
                    "IF-MIB::ifDescr.1","s",'"vlan1"',"IF-MIB::ifType.1","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"vlan2"',"IF-MIB::ifType.2","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.3", "i", "3",
                    "IF-MIB::ifDescr.3","s",'"vlan3"',"IF-MIB::ifType.3","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.4", "i", "4",
                    "IF-MIB::ifDescr.4","s",'"vlan4"',"IF-MIB::ifType.4","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.5", "i", "5",
                    "IF-MIB::ifDescr.5","s",'"vlan5"',"IF-MIB::ifType.5","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.6", "i", "6",
                    "IF-MIB::ifDescr.6","s",'"vlan6"',"IF-MIB::ifType.6","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.7", "i", "7",
                    "IF-MIB::ifDescr.7","s",'"vlan7"',"IF-MIB::ifType.7","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.8", "i", "8",
                    "IF-MIB::ifDescr.8","s",'"vlan8"',"IF-MIB::ifType.8","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.9", "i", "9",
                    "IF-MIB::ifDescr.9","s",'"vlan9"',"IF-MIB::ifType.9","i","7"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.10", "i", "10",
                    "IF-MIB::ifDescr.10","s",'"vlan10"',"IF-MIB::ifType.10","i","7"])
    
# Reinicio en caliente de la interfaz de un dispositivo de forma continuada
def pipeline4():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"eth0"',"IF-MIB::ifType.2","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"eth0"',"IF-MIB::ifType.2","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"eth0"',"IF-MIB::ifType.2","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"eth0"',"IF-MIB::ifType.2","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"eth0"',"ifType.1","i","4"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"eth0"',"IF-MIB::ifType.2","i","4"])
    
# Simula que un reinicio continuo del dispositivo de red
def pipeline5():
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])
    subprocess.call(["snmptrap", '-v', '1', '-c', 'public', '127.0.0.1', "coldStart", '0', '0', 'sysUpTime.0', "0"])

# Reinicio en caliente de varias interfaces de un dispositivo
def pipeline6():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/1"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/1"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"Fa0/0/2"',"ifType.1","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"Fa0/0/2"',"IF-MIB::ifType.2","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"FC-PH"',"ifType.1","i","56"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"FC-PH"',"IF-MIB::ifType.2","i","56"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/2"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/2"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"Fa0/0/1"',"ifType.1","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"Fa0/0/1"',"IF-MIB::ifType.2","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/1"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/1"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::warmStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkUp", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])

# Simula varios fallos de autenticaion en diferentes servidores
def pipeline7():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 1'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 2'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 1'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 3'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 2'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 2'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 2'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 1'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 3'"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1", "''", "SNMPv2-MIB::authenticationFailure", 
                        "SNMPv2-MIB::sysLocation.0", "s", "'Authentication Failure on Server 2'"])
    
# Simula el reinicio continuo sin que se puedan levantar definitivamente varias interfaces
def pipeline8():
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/1"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/1"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"Fa0/0/1"',"ifType.1","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"Fa0/0/2"',"IF-MIB::ifType.2","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"FC-PH"',"ifType.1","i","56"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"FC-PH"',"IF-MIB::ifType.2","i","56"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/2"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/2"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"Fa0/0/1"',"ifType.1","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"Fa0/0/1"',"IF-MIB::ifType.2","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/2"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/1"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"G0/0/1"',"ifType.1","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"G0/0/1"',"IF-MIB::ifType.2","i","117"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"S0/0/2"',"ifType.1","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"S0/0/2"',"IF-MIB::ifType.2","i","144"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "SNMPv2-MIB::coldStart", "ifIndex.2", "i", "2",
                     "ifDescr.1","s",'"Fa0/0/1"',"ifType.1","i","62"])
    subprocess.call(["snmptrap", "-v", "2c", "-c", "public", "127.0.0.1" ,"''", "IF-MIB::linkDown", "IF-MIB::ifIndex.2", "i", "2",
                    "IF-MIB::ifDescr.2","s",'"Fa0/0/1"',"IF-MIB::ifType.2","i","62"])
    
def main():
    pipeline8()
    print("SALIDA")

main()