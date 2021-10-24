def get_pay(value):
    pay=value
    return value

basic_pay=input('Enter Basic Pay:')
basic_pay_value=get_pay(basic_pay)

london_weighting=input('Enter London Weighting:')
london_weighting_value=get_pay(london_weighting)

gross_pay=basic_pay_value+london_weighting_value
print(gross_pay)
