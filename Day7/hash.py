#hash table

student_ids = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

student_id = int(input("Enter student ID to search: "))

if student_id in student_ids:
    print("Student found:", student_ids[student_id])
else:
    print("Student ID not found")



#Hash Maps

scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print(scores["Bob"])



#hash set

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)

# hash function
def hash_function(key, table_size):
    return key % table_size