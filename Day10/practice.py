def print_array(arr, index):
    if index == len(arr):
        return

    print(arr[index])
    print_array(arr, index + 1)


arr = [10, 20, 30, 40, 50]
print_array(arr, 0)



num =int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("factorial : ", factorial )    