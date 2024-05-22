my_ipaddr = input("\n Please enter an IP address to be converted Hex and Binary\n:")

ip_list = my_ipaddr.split(".")

print()
print(f'{"Octet1":^15} {"Octect2":^15} {"Octect3":^15} {"Octect4":^15}')
print("-" * 60)
print(f'{ip_list[0]:^15} {ip_list[1]:^15} {ip_list[2]:^15} {ip_list[3]:^15}')
print(f'{bin(int(ip_list[0])):^15} {bin(int(ip_list[1])):^15}' f'{bin(int(ip_list[0])):^15} {bin(int(ip_list[1])):^15}')
print("-" * 60)
