import os
class Choice:
    def choice1(self):
        print ("ex: 192.168.0.1")
        ip = str(input('Enter Target IP :'))
        result = os.system('nmap ' + ip)
        print (result)

    def choice2(self):
        print ("ex: testwebsite.com")
        host = input('Enter Targat Website: ')
        result = os.system('nmap ' + host)
        print (result)

    def choice3(self):
        print ("ex: 192.168.0.1-100")
        ips = str(input('Enter IP range: '))
        result = os.system('nmap ' + ips)
        print (result)

    def choice4(self):
        print ("ex: 192.168.1.0/24")
        subn = str(input('Enter IP Subnet range: '))
        result = os.system('nmap ' + subn)
        print (result)

    def choice5(self):
        print ("ex: port:22 ip:192.168.0.1")
        port = str(input('Enter Target Port: '))
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -p ' + port +' '+ip)
        print (result)

    def choice6(self):
        print ("ex: port:1-25 ip:192.168.0.1")
        ports = str(input('Enter Range of Port: '))
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -p ' + ports +' '+ip)
        print (result)

    def choice7(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -F ' + ip)
        print (result)

    def choice8(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -p- ' + ip)
        print (result)

    def choice9(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sT ' + ip)
        print (result)

    def choice10(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sS ' + ip)
        print (result)

    def choice11(self):
        print ("ex: port:22,23,25  ip:192.168.0.1")
        ports = str(input('Enter Target Ports: '))
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sU '+ ports +' ' + ip)
        print (result)

    def choice12(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -Pn -F ' + ip)
        print (result)

    def choice13(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -A ' + ip)
        print (result)

    def choice14(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sV ' + ip)
        print (result)

    def choice15(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sV --version-intensity 5 ' + ip)
        print (result)

    def choice16(self):
        print ("ex: Just Enter the Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sV --version-intensity 0 ' + ip)
        print (result)

    def choice17(self):
        print ("ex: Just Enter Target IP")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap -sV -p 443 --script=ssl-heartbleed '+ ip)
        print (result)

    def choice18(self):
        print ("ex: ip:192.168.0.1/24")
        ip = str(input('Enter Target IP: '))
        result = os.system('nmap --script=asn-query,whois,ip-geolocation-maxmind ' + ip)


