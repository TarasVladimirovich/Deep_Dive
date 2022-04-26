print(10 / 3)
print(10 // 3)
print(10 % 3)


def big_year(year):
    return 'yes' if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0) else 'no'


def big_year1(year):
    return 'yes' if not (year % 400) or not (year % 4) and (year % 100) else 'no'


print(big_year(2020) == big_year1(2020), big_year(2020))
print(big_year(2024) == big_year1(2024), big_year(2024))
print(big_year(400) == big_year1(400), big_year(400))
print(big_year(100) == big_year1(100), big_year(100))
print(big_year(1700) == big_year1(1700), big_year(1700))
print(big_year(2021) == big_year1(2021), big_year(2021))
