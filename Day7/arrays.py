# search by index
arr = [10, 20, 30, 40, 50]

a = int(input("enter indx to access:"))

print(arr[a])


# using loop traverse each

ar = [5, 10, 15, 20]

for i in ar:
    print(i)
    
    
    
#insert a number
arrr = [10, 20, 40, 50]
print(arrr)
arrr.insert(2, 30)
print(arrr)    



# inear search 

array = [4, 8, 15, 16, 23, 42]

x = int(input("enter number to search:"))

if x in array:
    print("found at ", array.index(x))
    
else:
    print("not found")    
    
    
    
# bubble sort

array1 = [5, 2, 8, 1, 3]

for i in range(len(array1)):
    for j in range(0, len(array1)-i-1):
        if array1[j]>array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]    
            print(array1)
            
            
            
# two pointer method 

array2 = [1, 2, 4, 6, 8, 9]

left = 0
right = len(array2) - 1

while left < right:
    current_sum = array2[left] + array2[right]
    if current_sum == 10:
        print("Pair found:", array2[left], array2[right])
        break
    elif current_sum < 10:
        left += 1
    else:
        right -= 1
else:
    print("No pair found")


