##SIMPLE PASSWORD GENERATOR
import random, time as t 
##
def generator(length):
    password = ""
    for i in range(length):
        password += chr(random.randint(33, 126))
    return password
##
start_time = t.time()
password_length = int(input("Enter the length of the password: "))
password_quantity = int(input("How many passwords do you want to generate? "))
##
for i in range(password_quantity):
    password = generator(password_length)
    print(password, end="\n")
    t.sleep(0.1)
##
end_time = t.time()
print("Time elapsed: ", end_time - start_time)
input("Press any key to exit...")
##