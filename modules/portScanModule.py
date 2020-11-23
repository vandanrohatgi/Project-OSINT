import socket

commonPorts=['21', '22', '23', '25', '53', '79', '80', '81', '88', '110', '111','113', '119', '123',
         '137', '138', '139', '143', '161', '179','389', '443', 
        '445', '465', '512', '513', '514', '515', '3306',
        '5432', '1521', '2638', '1433', '3389', '5900', '5901', '5902','5903', '5631', '631',
        '636','990', '992', '993', '995', '1080', '8080', '8888', '9000']

def portScan(target):
    ports=[]
    ip=socket.gethostbyname(target)
    for port in commonPorts:
        try :
            print("check for port: {}".format(port))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip,int(port)))
            ports.append(port)   
            sock.close()
        except socket.error:
            pass
    print(ports)
    

portScan('localhost')


















'''os.system("nmap -T4 -Pn --open {} | grep open | cut -d' ' -f1 | cut -d'/' -f1 > ports.txt".format(target))
if (os.path.exists('ports.txt')):
    f=open('ports.txt','r')
    ports=f.read()
    f.close()
    os.remove('ports.txt')
    print(ports)
else:
    return None'''











