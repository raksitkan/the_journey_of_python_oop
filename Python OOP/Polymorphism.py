#Overloading

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
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

    #salary year and bonus
    def _getIncome(self,bonus=0):
        return (self.__salary*12)+bonus
    
    def __str__(self):
        return (f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self._department} รายได้ต่อปี {self._getIncome()}")

#class ลูก
class Accounting(Employee):
    __departmentName = "บัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)#construtor class แม่
        self._age = age
    #OverRiding
    def _showdetail(self):
        super()._showdetail()
        print("อายุ = "+str(self._age))
        print("รายได้ต่อปี = "+str(super()._getIncome()))
        print("###############")


class Programmer(Employee):
    __departmentName = "พัฒนาระบบ"
    def __init__(self,name,salary,exp,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = exp
        self.__skill = skill
        #OverRiding
    def _showdetail(self):
        super()._showdetail()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print("รายได้ต่อปี = "+str(super()._getIncome()))
        print("###############")

class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area
        #OverRiding
    def _showdetail(self):
        super()._showdetail()
        print("พื้นที่รับผิดชอบ = "+self.__area)
        print("รายได้ต่อปี = "+str(super()._getIncome(10000)))
        print("###############")

accounting = Accounting("kon",15000,26)
accounting._showdetail()

programmer = Programmer("นัท",30000,0,"pytorch")
programmer._showdetail()

sale = Sale("โบว์วี่",20000,"บางปะกง")
sale._showdetail()




