from __future__ import unicode_literals, print_function

houston_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.40.1',
    '10.10.50.1',
    '10.10.60.1',
    '10.10.70.1',
    '10.10.80.1',
    '10.10.10.1',
    '10.10.20.1',
    '10.10.70.1',
]

atlanta_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.30.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.160.1',
    '10.10.170.1',
    '10.10.180.1',
]

chicago_ips = [
    '10.10.10.1',
    '10.10.20.1',
    '10.10.140.1',
    '10.10.150.1',
    '10.10.210.1',
    '10.10.220.1',
    '10.10.230.1',
    '10.10.240.1',
]


houston_set = set(houston_ips)
atlanta_set = set(atlanta_ips)
chicago_set = set(chicago_ips)


common_all = houston_set & atlanta_set & chicago_set
for i in common_all:
    print(i)
