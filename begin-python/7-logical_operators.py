has_high_income = True
has_good_credit = True
has_criminal_record = True
####logical and both should be true
####logical OR one of them should be true
## NOT convert to boolean

if has_high_income and has_good_credit:
    print("The person is Eligible for loan")

if has_high_income and not has_criminal_record:
    print("The person is Eligible for loan")
