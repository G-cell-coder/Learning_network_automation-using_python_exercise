from __future__ import unicode_literals, print_function

net_device = {
    'ip_addr': '10.10.10.10',
    'vendor':'cisco',
    'username':'admin',
    'password': 'password'
    }

print()
print(net_device['ip_addr'])
print()

if net_device['vendor'].lower() == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['vendor'].lower() == 'juniper':
    net_device['platform'] = 'junos'

bgp_fields={
    'bgp_as': 42,
    'peer_As':100,
    'peer_ip': '172.16.31.100',
}

net_device.update(bgp_fields)

print('-'*80)
for key in net_device:
    print("{:>15}".format(key))
print('-'*80)
print()

print('-' * 80)
for key,value in net_device.items():
    print("{:>15}".format(key))

print('-'*80)
print()

print('-'*80)

for key, value in net_device.items():
    print("{key:>15} ---> {value:>15}".format(key=key,value=value))

print('-'*80)
print()
