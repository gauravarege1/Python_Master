## Error handel  and ouput is shown in readable format.

import paramiko
p = paramiko.SSHClient()
server_list = open("serverlist.csv","r")  ##mention server ip and user name & p/w in csv file
for i in server_list.readlines():
    try:
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
    except Exception as error:
        print(error)
server_list.close()