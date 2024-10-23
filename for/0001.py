for n in range (2004, 2100):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print(n)
