from employee import Employee

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