def add(x,y):
    return x+y # This program is for addition two nymbers

def sub(x,y):
    return x-y # This program is for subtract two nymbers

def mul(x,y):
    return x*y # This program is for  multiplication two nymbers

def div(x,y):
    return x/y  # This program is for division two nymbers


print("Select ehe operation : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter the choice(1,2,3,4): ")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter First number: "))
        num2 = float(input("Enter Second number: "))

        if choice =='1':
                     print(num1, "+", num2, "=", add(num1,num2))
        elif choice =='2':
                     print(num1, "-", num2, "=", sub(num1,num2))
        elif choice =='3':
                     print(num1, "*", num2, "=", mul(num1,num2))
        elif choice =='4':
                     print(num1, "/", num2,"=", div(num1,num2))
        break
    else:
        print("invalid input")
