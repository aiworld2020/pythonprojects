#asks user for the number in fibonacci sequence
number = int(input("Enter a positive number and I will give you the number in the fibonacci sequence that is your number: "))
#tests whether number is positive
while(True):
    if number <= 0:
        print("You didn't enter a positive number, try again")
        number = int(input("Enter a positive number and I will give you the number in the fibonacci sequence that is your number: "))
        continue
    else:
        break

##1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
x = 0
y = 1
fib_list=[1,1]
for i in range(1,number-1):
    sum = fib_list[-1] + fib_list[-2]
    fib_list.append(sum)  
print(fib_list[number-1 ])

    
