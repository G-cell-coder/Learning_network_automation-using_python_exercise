from __future__ import unicode_literals, print_function

import re

show_version = """
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
"""

match1 = re.search(r".(\d{3})\W.*",show_version)
print(match1.group(1))
print("Model number identified from the version:\n", match1.group(1))

match2 = re.search(r".(\d*K\/\d*K)\W.*",show_version)
print("Memory associated with this model is:\n", match2.group(1))
