from __future__ import print_function, unicode_literals

with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()
#print(show_ip_int_brief)

fa4_ip = show_ip_int_brief[5].strip()
print(fa4_ip)
'''
fields = fa4_ip.split()
intf = fields[0]
ip_address = fields[1]
my_results = (intf, ip_address)
print(my_results)
'''
