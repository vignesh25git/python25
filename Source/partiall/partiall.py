from functools import partial


def calculate_final_total(price,tax_percent):
    total = price * ( 1 + tax_percent/100)
    return total

print(calculate_final_total(100,18))

changed_func = partial(calculate_final_total,tax_percent=18)

print(changed_func(100))