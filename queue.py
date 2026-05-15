# Queue Management System

queue = []
MAX = 5

def enqueue():
    if len(queue) >= MAX:
        print("Queue Overflow")
    else:
        val = input("Enter values: ").split()
        queue.extend(val)
        print("Elements inserted successfully")

def dequeue():
    if not queue:
        print("Queue Underflow")
    else:
        print("Removed:", queue.pop(0))

def front():
    if not queue:
        print("Queue is empty")
    else:
        print("Front Element:", queue[0])

def rear():
    if not queue:
        print("Queue is empty")
    else:
        print("Rear Element:", queue[-1])

def display():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue Elements:")
        for i in queue:
            print(i)

def size():
    print("Queue Size:", len(queue))

while True:
    print("\n===== QUEUE MENU =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Display")
    print("6. Size")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()

    elif ch == 2:
        dequeue()

    elif ch == 3:
        front()

    elif ch == 4:
        rear()

    elif ch == 5:
        display()

    elif ch == 6:
        size()

    elif ch == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")