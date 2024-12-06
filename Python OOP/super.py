#super เมื่อต้องการเรียกใช้งานคุณสมบัติต่างๆของคลาสแม่เช่น construtor method attribute
#การสืบทอดคุณสมบัติ (Inheritance)
#class แม่
class Employee:
    #class variable
    minsalary = 50000
    _maxsalary = 50000
    companyName = "ABC.co.lt"
    def __init__(self,name,salary,department):#construtor
        # instance variable
        self.__name = name #Private
        self.__salary = salary #Private
        self._department = department #Private
    
    # Private method
    def _showdetail(self):
        print(f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self._department}")
    #salary per year
    def _getIncome(self):
        return self.__salary*12
    
    def __str__(self):
        return (f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self._department} รายได้ต่อปี {self._getIncome()}")
#class ลูก
class Accounting(Employee):
    __departmentName = "บัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):
    __departmentName = "พัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        # super()._showdetail()

class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)


accounting = Accounting("kon",15000)
# print(f"รายได้ต่อปี {accounting._getIncome()}")
print(accounting.__str__())
programmer = Programmer("นัท",30000)
print(programmer.__str__())
sale = Sale("โบว์วี่",20000)
print(sale.__str__())
# programmer._showdetail()



