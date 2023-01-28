## %s"%ls[0] is veriable  and it's read by  first index like server ip 
## username = "%s"%ls[1]  and it's read by  second  index like users name 

import paramiko
p = paramiko.SSHClient()
server_list = open("serverlist.csv","r")  ##mention server ip and user name & p/w in csv file
for i in server_list.readlines():
    line=i.strip() 
    ls =line.split(",")
    print(ls)
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect("%s"%ls[0],port =22, username = "%s"%ls[1], password="%s"%ls[2])
    stdin, stdout, stderr = p.exec_command("uname -a ; df -h ; ifconfig ; cat /etc/hosts ; /etc/resolv.conf")
    opt = stdout.readlines()
    opt ="".join(opt)
    print(opt)
    temp=open("%s.txt"%ls[0],"w")
    temp.write(opt)
    temp.close()
server_list.close()
