# Stack Management System

stack = []
MAX = 5

def push():
    if len(stack) >= MAX:
        print("Stack Overflow")
    else:
        val = input("Enter values: ").split()
        stack.extend(val)
        print("Elements pushed successfully")

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Removed:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top Element:", stack[-1])

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack Elements:")
        for i in reversed(stack):
            print(i)

def size():
    print("Stack Size:", len(stack))

while True:
    print("===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        push()

    elif ch == 2:
        pop()

    elif ch == 3:
        peek()

    elif ch == 4:
        display()

    elif ch == 5:
        size()

    elif ch == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")