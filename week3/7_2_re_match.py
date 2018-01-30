import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

print(type(match))
print(match.start())
print(match.end())
string_todo = 'BIT 100081'
print(string_todo[match.start():match.end()])
print(match.span())

print('**********************************************')
match = re.search(r'PY.*N', 'PYANBNCNDN')
print(match.group(0))
