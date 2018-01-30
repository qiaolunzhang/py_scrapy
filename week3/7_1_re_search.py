import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')

if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', 'BIT 100081')

if match:
    match.group(0)

ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

split_string = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(split_string)

split_string = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
print(split_string)

print('*************************************************')
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))

print('********************************************')
sub_string = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
print(sub_string)

print('********************************************')
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT 100081')
print(rst.group(0))

print('**************************************')