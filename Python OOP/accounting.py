from employee import Employee
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

