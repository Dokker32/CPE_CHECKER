import telnetlib
import random
import time 
import string

HOST = input(str('Host: '))

s = (str('flash set DEF_WLAN1_SSID '))
ch =(str('flash set WLAN1_CHANNEL '))



tn = telnetlib.Telnet(HOST)
tn.read_until(b"rlx-linux login: ")
tn.write(b'admin\n')
tn.read_until(b"Password: ")
tn.write(b'password\n')
time.sleep(3)
print('Authorized')

def rand(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))
	
while True:
	tn.read_until(b"$ ")
	tn.write(b's + rand(10)\n')
	time.sleep(10)
	tn.write(b'ch + rand(2)\n')
	time.sleep(10)
	



d1_contents = set(os.listdir('example/dir1'))
d2_contents = set(os.listdir('example/dir2'))
common = list(d1_contents & d2_contents)
common_files = [

f
for f in common
if os.path.isfile(os.path.join('example/dir1', f))
]
print('Common files:', common_files)
