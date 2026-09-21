def PrintEven(n):
    if n == 0:
        return

    PrintEven(n - 1)

    if n % 2 == 0:
        print(n)

PrintEven(5)


def PrintReverse(n):
    # write your recursive logic here
    if n == 0:
        return
    print(n)
    PrintReverse(n - 1)

PrintReverse(5)