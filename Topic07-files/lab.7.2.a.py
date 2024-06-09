FILENAME = "count.txt"
def readNumber():
     with open(FILENAME) as f:
        number = int(f.read())
        return number 
num = readNumber()
print (num) 


