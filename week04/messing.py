#FILENAME = "hiBaby.txt"
#with open(FILENAME, 'x') as f:
#    f.write("Hi, baby!")

#FILENAME = "test.txt"
#with open(FILENAME, 'w' ) as f:
#  f.write('Hello, darling')
#import os 
#filename="test.txt"
#if os.path.exists(filename):
#    print (filename, "already exists")
#else:
#    print(filename, "does not exist do you want to create it?")
with open("test-b.txt", "w") as f:
    data = f.write("test b\n")
    print (data)
with open("test-b.txt", "a") as f2:
    data = f2.write("another line\n")
    print (data) 
 