from empmgmt import Empmgmt

if(__name__ == "__main__"):
    object1 = Empmgmt()
    ch = 0
    while(ch != 6):
        print('''
                1.Add New Emp
                2. Display Details
                3. Search
                4. Delete
                5. Update
                6. Exit
                ''')
        ch = int(input("Enter your choice: "))
        if(ch == 1):
            object1.addEmp()
        elif(ch == 2):
            object1.display()
        elif(ch == 3):
            id = int(input("Enter the id to be search: "))
            object1.search(id)
        elif(ch == 4):
            id = int(input("Enter the id to be deleted: "))
            object1.delete(id)
        elif(ch==5):
            id = int(input("Enter the id to be updated: "))
            object1.update(id)
        elif(ch==6):
            print("Exiting...")