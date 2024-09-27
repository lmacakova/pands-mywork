import json
FILENAME = "storedata.json"

def displayMenu():
     print("What would you like to do?")
     print("\t(a) Add new student") 
     print("\t(v) View students") 
     print("\t(q) Quit") 
     choice = input("Type one letter (a/v/q):").strip()

     return choice 

def readModules(): 
    return []

def doAdd (students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :") 
    currentStudent["modules"]= readModules() 
    students.append(currentStudent)   

def readModules():
    modules = [] 
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "": 
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def displayModules(modules): 
    print ("\tName \tGrade")
    for module in modules: 
        print(f"\t{ module['name']} \t{ module['grade']}")

def doView(students): 
    for currentStudent in students:
        print(currentStudent["name"]) 
        displayModules(currentStudent["modules"])
    print(students)

def doSave(students):  
    #you will put the call to save dict here  
    with open(FILENAME, 'w') as f:
        json.dump(obj,f)   
writeDict(students)
print("students saved") 
     
def doLoad:
    with open(FILENAME) as f:
        return json.load(f)
students = doLoad() 


 #main program 
students= []    
choice = displayMenu() 
while(choice != 'q'): 
# we could do this with lambda functions 
# I am keeping this basic for the moment
    if choice == 'a': 
        doAdd(students) 
    elif choice == 'v': 
        doView(students) 
    elif choice !='q': 
        print("\n\nplease select either a,v or q") 

    choice = displayMenu()
