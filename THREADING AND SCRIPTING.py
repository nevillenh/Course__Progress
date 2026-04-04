  # THREADING
import threading
import time 
done = False
def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
thread = threading.Thread(target=worker).start()
input ("Press Enter to stop...\n")
done = True


def task():
    for i in range(5):
        print("Task running")

# Create thread
t1 = threading.Thread(target=task)

# Start thread
t1.start()

t1.join()

print("Done")

# MULTI-THREADING
def task1():
    for i in range(5):
        print("Task 1 running")

def task2():
    for i in range(5):
        print("Task 2 running")

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Done")
# example 2
import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C']:
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# SCRIPTING
import os
# Get current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)
# List files in the current directory
files = os.listdir(cwd)
print("Files in the current directory:", files)
# Create a new directory
os.mkdir("new_directory")
print("New directory created.")
# Remove the created directory
os.rmdir("new_directory")
print("New directory removed.")

# File auomation
with open("example.txt", "w") as file:
    file.write("Hello, this is a scripted file.\n")
    file.write("This file was created using Python scripting.\n")
print("File 'example.txt' created and written to.")

    

# THREADING AND SCRIPTING TOGETHER
import threading
import time
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)
def print_letters():
    for letter in ['A', 'B', 'C']:
        print(letter)
        time.sleep(1)
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
t1.join()
t2.join()
print("Done")
