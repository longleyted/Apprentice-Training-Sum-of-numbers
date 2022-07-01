x = 0
y = 0
while True: 
    if x % 4 == 0:
        print("Missing ", x,"th number")
        x += 1
    else:
        y = y + x
        x+=1
        if x == 100:
            print("The total sum is: ",y)
            break
