from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"


mac_ent = [mac1, mac2, mac3]
mp2 = []
for mac in mac_ent:
    mp1 = mac.split()
    mp2.append(mp1[1])
    mp2.append(mp1[3])

print(mp2)

print(f'{"     ":^8} {"IP ADDR":^16} {"MAC address":^8}')
print("-"* 32)
for i in range(0,len(mp2),2):
    print("\t"+mp2[i]+"\t"+mp2[i+1])

