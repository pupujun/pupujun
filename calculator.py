def calculator(codes,salarys):
    
        a = b * 0.835 - 3500

        if a <= 0:
            tax = 0
        elif a <= 1500:
            tax = a * 0.03

        elif a <= 4500:
            tax = a * 0.1-105

        elif a <= 9000:
            tax = a * 0.2 - 555

        elif a <= 35000:
            tax = a * 0.25 - 1005

        elif a <= 55000:
            tax = a * 0.3 - 2755

        elif a <= 80000:
            tax = a* 0.35 - 5505

        else:
            tax = a * 0.45 - 13505

        aftersalary = b * 0.835 - tax

        format(aftersalary,'2f')

        print('{}:{:.2f}'.format(codes,aftersalary))

if __name__ == '__main__':

    import sys

    for arg in sys.argv[1:]:

        code_salary = arg.split (':')

        code = code_salary[0] 
        
        salary = code_salary[1]

        try:
            b = int(salary)
    
            c = int(code)
        except:
            print("Parameter Error")

        calculator(c,b)

