class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return str(self.id)+","+self.name+","+str(self.salary)+"\n"