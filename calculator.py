import sys

salary = sys.argv[1]

try:
   b = int(salary)

except:
    print("Parameter Error")

a = b - 3500

if a <= 1500:
    tax = a * 0.03
    print(format(tax,".2f"))

elif a <= 4500:
    tax = a * 0.1-105
    print(format(tax,".2f"))

elif a <= 9000:
    tax = a * 0.2 - 555
    print(format(tax,".2f"))

elif a <= 35000:
    tax = a * 0.25 - 1005
    print(format(tax,".2f"))

elif a <= 55000:
    tax = a * 0.3 - 2755
    print(format(tax,".2f"))

elif a <= 80000:
    tax = a* 0.35 - 5505
    print(format(tax,".2f"))

else:
    tax = a * 0.45 - 13505
    print(format(tax,".2f"))
