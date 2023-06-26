import re

string = "32d 10h 54m"
pattern = r'\d+(?=d)'
match = re.findall(pattern, string)
print(match)


time_string = "12d 45h 734m 223s"
reversed_string = time_string[::-1]
print(reversed_string)


l1 = [1, 2]
l2 = [3, 4]

l1 = l1.__add__[l2]

print(l1)
