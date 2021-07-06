import os
import time

print('\n\n\t\t\tMAC CHANGER by DEV')
time.sleep(3)

while True:
	print('\n\n\t\tMac is changing\t\t\n')
	os.system('ifconfig eth0 down')
	os.system('macchanger -r eth0')
	os.system('ifconfig eth0 up')
	time.sleep(1)	