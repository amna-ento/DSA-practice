# queue

que = [10, 20, 30]

def enqueue(item):
    que.append(item)

def dequeue():
    if que:
        return que.pop(0)
    else:
        return "Queue is empty"

print(enqueue(40))
print(enqueue(50))
print(dequeue())



#stack

stack = [10, 20, 30]

def push(item):
    stack.append(item)

def pop():
    if stack:
        return stack.pop()
    else:
        return "Stack is empty"

push(40)
pop()
push(50)

print(stack)






