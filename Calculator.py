def add (P,Q):
    return P+Q
def substract (P,Q):
    return P-Q
def multiply (P,Q):
    return P*Q
def divide (P,Q):
    return P/Q
print("please select the operation.")
print("a.add")
print("b.substact")
print("c.multiply")
print("d.divide")
choice=input("please enter the choice(a/b/c/d):")
num_1=int(input("please enter the first number:"))
num_2=int(input("please enter the second number:"))
if choice == 'a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == 'b':
    print(num_1,"-",num_2,"=",subsrtact(num_1,num_2))
elif choice == 'c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice == 'd':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("invalid input")