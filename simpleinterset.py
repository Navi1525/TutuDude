"""
simpleinterest = (p*r*t)/100;

"""
Principal=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time of interest: "))

SI=(Principal*rate*time)/100

print("SI is ",SI)

amount=Principal*(1+rate/100)**time

CI=amount-Principal
print("Compound Interest :",round(CI,2))
print("Compound Interest :",round(CI,))