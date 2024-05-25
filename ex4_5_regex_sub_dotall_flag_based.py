import re

with open('show_ip_v6_intf.txt','r') as f:
   rl =  f.read()
#   print(rl)
   pm = re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:",rl, flags=re.DOTALL)
   ipv6_add = pm.group(1).strip()
   print(ipv6_add.splitlines())


for i in ipv6_add.splitlines():
   tp = re.sub(r"\[VALID\]","",i)
   print(tp.strip()) 
