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