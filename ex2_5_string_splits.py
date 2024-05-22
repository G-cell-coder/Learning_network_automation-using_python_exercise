from __future__ import print_function, unicode_literals

with open('show_ip_bgp_sum.txt') as f:
    bgp_lines = f.readlines()


print(bgp_lines)
print("First line of show ip bgp summ:\n", bgp_lines[0])
print("Last line of show ip bgp summ:\n",bgp_lines[-1])

f_bgp = bgp_lines[0]
l_bgp = bgp_lines[-1]

f_bgp = f_bgp.split(" ")
as_bgp = f_bgp[-1]
l_bgp = l_bgp.split(" ") 
ip_bgp = l_bgp[0]

print("As number from the show ip bgp summ is:\n",as_bgp)
print("The IP address of the show ip bgp summ is:\n", ip_bgp)
