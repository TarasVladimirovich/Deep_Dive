import re
text = 'qwerty dmvnbsdfmd zslksjhfdskj kyiv ldfkjsjh dsfjkh 555-555-55-55 kyiv qwerty takkoe'
match = re.search('qwerty', text)
print(match)
print(match.span())
print(dir(match))
print(match.regs)
matches = re.findall('qwerty', text)
print(matches)
print(type(matches))
ma = re.finditer('kyiv', text)
print(ma)
print(next(ma).span())
print(next(ma).group())