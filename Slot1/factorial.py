def checkInput(prompt):
    x = input(prompt)
    flag = 0
    while(flag == 0):
        try: x = int(x)
        except: 
            print("Error, please enter numeric input")
            x = input(prompt)
        else: 
            flag = 1
    return int(x)

n = checkInput("n = ")
f = 1
for i in range(1, n+1):
    f = f * i

print("n! = ", f)