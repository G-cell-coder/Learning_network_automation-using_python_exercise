from __future__ import unicode_literals, print_function

with open('show_arp.txt') as f:
   arp_lines = f.readlines()

arp_lines = arp_lines[1:]
present1,present2 = 1,1
for line in arp_lines:
    arp_col = line.split(" ")
    if arp_col[2] == "10.220.88.1":
        print("Default gateway IP is : {0} and MAC is : {1}".format(arp_col[2],arp_col[16]))
        present1 = 0
    elif arp_col[2] == "10.220.88.30":
        print("Arista3 IP is : {0} and MAC is : {1}".format(arp_col[2],arp_col[15]))
        present2 = 0 
if (present1 and present2) :  
    print("No detail available:\n")

    
