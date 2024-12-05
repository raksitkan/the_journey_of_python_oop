#
#Private(__)
class Employee:
    def __init__(self,name,salary,department):
        # Private attribute
        self.__name = name #Private
        self.__salary = salary #Private
        self.__department = department #Private
    # Private method
    def _showdetail(self):
        print(f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self.__department}")
    #setter method
    def setName(self,newname):
        self.__name = newname
        return self.__name

    def setSalary(self,newsalary):
        self.__salary = newsalary
        return self.__salary

    def setDepartment(self,newdepartment):
        self.__department = newdepartment
        return self.__department
    
    #getter method
    def getName(self):
        return self.__name
    
obj1 = Employee(name="กร",
                salary=50000,
                department="CEO")
# obj1.setName(newname="กรซ่า")
# obj1.setSalary(newsalary=75000)
# obj1.setDepartment(newdepartment="it")
print(f"พนักงานมาทำงานเร็วที่สุด = {obj1.getName()}")
obj1._showdetail()