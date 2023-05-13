def fib(n:int)->int:
    """
    Function that returns the n-numbers of Fibonacci sequence

    params: n -> length of the sequence
    returns: n -> numbers of Fibonacci sequence    
    """
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n<0:
        print("The number cant be negative")
        raise ValueError
    else:
        pass
    x=y=1
    print(1,1,sep = "\n")
    for i in range(0,n-2):
        z=x + y
        yield z
        x=y
        y=z