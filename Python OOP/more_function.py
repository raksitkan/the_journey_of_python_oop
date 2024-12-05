#ฟังชั่นเสริม
class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def showdetail(self):
        print(f"ชื่อพนักงาน {self.name} เงินเดือน {self.salary} แผนก {self.department}")
    # destrutor ไม่ระบุก็ได้ คือ คำสั่งคืนค่าหรือคืนแรม
    # def __del__(self):
    #     print("call Destructor")

#สร้างวัตถุ
obj1 = Employee(name="กร",
                salary=50000,
                department="CEO")
obj2 = Employee(name="โบว์",
                salary=50000,
                department="CFO")
obj3 = Employee(name="ปวิน",
                salary=50000,
                department="บัญชี")

#เช็คว่าวัตถุอยุ่ในคลาสหรือไม่ เช่น ถ้า obj1 ถูกสร้างโดย Employee()
#ถ้าเป็นจริงจะได้คำตอบ TRUE ถ้าไม่จะได้ False
print(isinstance(obj1,Employee))

#dir เช็คว่า มี method อะไรบ้าง dir()
print(dir(obj1))
#เช็คว่า obj1 มาจากคลาสอะไร .__class__
print(obj1.__class__)
