#class variable
class Employee:
    #class variable
    _minsalary = 12000
    _maxsalary = 50000
    _companyName = "ABC.co.lt"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name #Private
        self.__salary = salary #Private
        self._department = department #Private
    # Private method
    def _showdetail(self):
        print(f"ชื่อพนักงาน {self.__name} เงินเดือน {self.__salary} แผนก {self._department}")

obj1 = Employee(name="กร",
                salary=50000,
                department="CEO")

# print(obj1._department)
print(f"เงินเดือนต่ำสุดของพนักงาน : {Employee._minsalary}")
print(f"เงินเดือนมากสุดของพนักงาน : {Employee._maxsalary}")
print(f"บริษัท : {Employee._companyName}")
