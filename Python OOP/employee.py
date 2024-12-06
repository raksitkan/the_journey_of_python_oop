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