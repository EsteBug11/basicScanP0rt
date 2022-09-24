#create simple program for scan 1024 ports in ip address and show open ports
import socket,sys,threading,queue,time,os,subprocess,platform,socket,threading,queue,time,os,subprocess,platform

def scan(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip,port))
        print(port,"open")
        s.close()
    except:
        pass

def main():
    ip = input("Enter ip address: ")
    for port in range(1,65535):
        t = threading.Thread(target=scan,args=(ip,port))
        t.start()

if __name__ == "__main__":
    main()