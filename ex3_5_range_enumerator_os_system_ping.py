from __future__ import unicode_literals, print_function
import os

# Toggle this to use Windows
WINDOWS = False

base_ip = '10.10.100.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

# Only use IP addresses 8.8.4.3 to 8.8.4.6
ip_list = ip_list[2:6]

print()
print('-' * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_cmd, ip_addr))
    print('-' * 80)
print('-' * 80)
print()

