def collatz(n):
    if n <= 1:
        print("Enter a positive number greater than 1")
        return

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)


try:
    number = int(input("Enter a number: "))
    collatz(number)
except ValueError:
    print("Please enter a valid number")
