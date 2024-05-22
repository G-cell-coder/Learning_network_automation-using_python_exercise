import pathlib
import re

my_file ="show_version.txt"

with open(my_file) as sh_ver:
    sh_ver = sh_ver.read()

match1 = re.search(r".*Version(.*),(.*)", sh_ver)
print(" Version of the CISCO device: \t{}".format(match1.group(2)))

match2 = re.search(r".*(FTX\w*)", sh_ver)
print("Serial Number of CISCO device:\t{}".format(match2.group(1)))

match3 = re.search(r".* register is(.*)" , sh_ver)
print("Config Register: \t{}".format(match3.group(1)))

