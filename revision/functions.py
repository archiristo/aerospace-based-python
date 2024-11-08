##selamlayıcı ???

def greet(isim):
    print("hello ",isim)
greet("a")
greet("b")

## add, return
def add(a, b):
    return a + b
    
result = add(6,5)
print(str(result))

##deneme, hesap makinesi model-1
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
calc = int(input("+(1), -(2), /(3), *(4)"))
if calc > 4 or calc < 1:
    print("invalid answer")

if calc == 1:
    print("Answer: ",num1+num2)

elif calc == 2:
    print("Answer: ",num1-num2)

elif calc == 3:
    if num2 == 0:
        print("ERROR: There is no division by 0")

    else:
        print("Answer: ",num1/num2)

else:
    print("Answer: ",num1*num2)


##deneme, hesap makinesi model-2

a = 8
b = 2

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

print(add(a,b))
print(substract(a,b))
print(divide(a,b))
print(multiply(a,b))