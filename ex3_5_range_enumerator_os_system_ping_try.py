from __future__ import unicode_literals, print_function
import os

WINDOWS = False

base_ip = '10.10.100.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'

base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []

for i in range(1,255):
    ipa = base_ip+str(i)
    ip_list.append(ipa)

for n,i in enumerate(ip_list):
    print("{0} ---> {1}\n".format(n,i))



for i in range(1,255):
    os.system("ping -n 3 10.10.100.{}".format(i))
