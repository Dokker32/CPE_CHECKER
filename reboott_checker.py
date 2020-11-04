import telnetlib 
import time 
import string

ip = input(str('ip: '))

while True:
	tn = telnetlib.Telnet(ip)
	tn.write(b'192.168.1.1\n')
	print("Connected")
	tn.read_until(b"rlx-linux login:")
	tn.write(b'admin\n')
	print("Login ok")
	tn.read_until(b'Password: ')
	tn.write(b'password\n')
	print("password ok")
	tn.read_until(b'#')
	tn.write(b'reboot\n')
	print("Reboot OK")
	time.sleep(240)
else:
	print("Bug Detected")