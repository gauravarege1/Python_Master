## paramiko  Module
## it's use only one server i am find out  multiple server
## p=  object

import paramiko
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect ("192.168.1.***",port =22, username = "*****", password="****")
stdin, stdout, stderr = p.exec_command ('''cat /etc/fstab
cat /etc/hosts
ifconfig
df -h ''')
opt = stdout.readlines()
opt ="".join(opt)
print(opt)
