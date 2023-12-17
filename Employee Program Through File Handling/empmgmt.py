from emp import Employee

class Empmgmt:
    
    def addEmp(self):
        id = int(input("Enter the id: "))
        name = input("Enter the name: ")
        salary = int(input("Enter the salary: "))
        emp = Employee(id, name, salary)
        fp = open("text1.txt","a")
        fp.write(str(emp))
        fp.close()
    
    def display(self):
        with open("text1.txt","r") as fp:
            for e in fp:
                print(e)
                sep_text = e.split(',')
                print("id: ",sep_text[0])
                print("name: ",sep_text[1])
                print("salary: ",sep_text[2])
                print("--------------------------------")
    
    def search(self,id):
        with open("text1.txt","r") as fp:
            for e in fp:
                try:
                    e.index(str(id),0,4)
                    print("Employee Found")
                    break
                except ValueError:
                    pass
            else:
                print("Employee not Found")

    def delete(self,id):
        container = []
        found = False
        with open("text1.txt","r") as fp:
            for e in fp:
                sep_text = e.split(',')
                if sep_text[0] == str(id):
                    found = True
                else:
                    container.append(e)
                
        if(found == True):
            with open("text1.txt","w") as fp:
                for e in container:
                    fp.write(e)
                    
    
    def update(self,id):
        container = []
        found = False
        with open("text1.txt","r") as fp:
            for e in fp:
                sep_text = e.split(",")
                if(sep_text[0]==str(id)):
                    found = True
                    ans = input("Do you want to Change name: (y/n)")
                    if(ans == 'y'):
                        sep_text[1] = input("Enter new name: ")
                    ans = input("Do you want to Change salary: (y/n)")
                    if(ans == 'y'):
                        sep_text[2] = input("Enter new salary: ")
                        
                    e = ','.join(sep_text)
                
                container.append(e)
                
        if(found == True):
            with open("text1.txt","w") as fp:
                for e in container:
                    fp.write(e)
        else:
            print("Employee not Found")