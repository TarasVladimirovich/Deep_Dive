import re
text = "qwerty dmvnbsdfmd zslksjhfdskj kyiv ldfkjsjh dsfjkh 555-555-55-55 kyiv qwerty takkoe"
match = re.search("qwerty", text)
print(match)
print(match.span())
print(dir(match))
print(match.regs)
matches = re.findall("qwerty", text)
print(matches)
print(type(matches))
ma = re.finditer("kyiv", text)
print(ma)
print(next(ma).span())
print(next(ma).group())

te1 = "v1.21.11-hpe1"
te2 = "1.21"
pattern = r"^v?\d\.\d{1,2}.?"
# match = re.search(pattern, te1)
# q = match.group()[:-1].replace("v", "")
# print(q)
match = re.search(pattern, te2)
q = match.group().replace("v", "")
if q.endswith("."):
    q = q[:-1]
print(q)
