#การสืบทอดคุณสมบัติ (Inheritance)
#class แม่
class Employee:
    #class variable
    minsalary = 50000
    _maxsalary = 50000
    companyName = "ABC.co.lt"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name #Private
        self.__salary = salary #Private
        self._department = department #Private
    # Private method
    def _showdetail(self):
        print(f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self._department}")

#class ลูก
class Accounting(Employee):
    departmentName = "บัญชี"
    def __init__(self):
        pass
class Programmer(Employee):
    departmentName = "พัฒนาระบบ"
    def __init__(self):
        pass
class Sale(Employee):
    departmentName = "ฝ่ายขาย"
    def __init__(self):
        pass


programmer = Programmer()
print(programmer.companyName)



