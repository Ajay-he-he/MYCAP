def fibonacci(num):
    data = [0, 1]
    num-=2      #Inorder to accomodate the user's length choice
    for _ in range(num):
        length = len(data)
        new=data[length-1]+data[length-2]
        data.append(new)
    print(f"Your fibonacci series is {data}")

val=int(input("How long do you want you fib series to be? "))
fibonacci(val)
