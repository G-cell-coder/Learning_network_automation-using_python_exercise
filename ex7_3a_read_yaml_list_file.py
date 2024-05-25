from __future__ import print_function, unicode_literals
import yaml

yaml_file = "ex7_3a_yaml_file.yml"

with open(yaml_file) as f:
    data = yaml.load(f)

print()
print(data)
print()
