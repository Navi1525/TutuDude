"""
semi perimeter =s =(a+b+c)/2;
area = sqrt(s(s-a)(s-b)(s-c))
"""
a=float(input("Enter the first side length: "))
b=float(input("Enter the second side length: "))
c=float(input("Enter the third side length: "))

s=(a+b+c)/2
print("Semi perimeter :",s)

area=(s*(s-a)*(s-b)*(s-c))  **0.5
print("Area of Triangle ",area)
print("Area of Triangle ",round(area,2))