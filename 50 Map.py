income = [10, 30, 100]


def double_money(dollars):
    return dollars * 2


new_income = list(map(double_money, income))

print(new_income)
