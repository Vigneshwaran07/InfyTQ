import re
inp = "someString&337"
match = re.findall(r'\d+',inp)
digits = sorted(set(list("".join(match))), reverse=True)
even_index = -1
for ind, i in enumerate(digits):
    if(int(i)%2==0):
        even_index = ind
if even_index == -1:
    print(-1)
else:
    digits[-1],digits[even_index] = digits[even_index],digits[-1]
    print(int(''.join(digits)))
