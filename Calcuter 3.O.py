first = input("Enter ur first number : ")
opreation = input("Enter ur opreation(+,-,*,/,%) : ")
second = input("Enter ur second number : ")
if opreation =='+':
    print(int(first) + int(second))
elif opreation =='-':
    print(int(first) - int(second))
elif opreation =='*':
    print(int(first) * int(second))
elif opreation =='/':
    print(int(first) / int(second))
elif opreation =='%':
    print(int(first) % int(second))
else:
    print("Invald Opreation")
exit("Thank You!!!!")
