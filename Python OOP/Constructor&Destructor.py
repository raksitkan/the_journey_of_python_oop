#การสร้าง construtor คือ การกำหนดค่าเริ่มต้นให้กับวัตถุ
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
#การปรับเปลี่ยนค่าหรืออัพเดท
obj1.salary = 70000
obj1.showdetail()
