from __future__ import print_function, unicode_literals
import random
import re
def generate_ip(network="10.10.10."):
    last = str(random.randint(1,254))
    return network+last


vip = generate_ip("192.168.0.")
vp = re.sub(r"\.0[0-9]$",".",vip)
print(vp)
valid_ip = generate_ip(network="171.128.30.0")

vp = re.sub(r"\.0",".",valid_ip)
print(vp)
