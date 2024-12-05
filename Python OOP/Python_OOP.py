# #สร้าง classพนักงาน
# class Employee:
#     #กำหนด Attribute โดยใช้ self. นำหน้า
#     #สร้าง method
#     def detail(self):
#         self.name = "raksitkan"
#         self.salary = 30000
#         print("ชื่อพนักงาน = {}" .format(self.name))
#         print("ชื่อพนักงาน = {}" .format(self.salary))

# #สร้างวัตถุหรือการเรียกใช้ -> emp1
# emp1 = Employee()
# emp1.detail()

# # เก็บข้อมูลหลายค่าใน class
class Employee:
    #กำหนด Attribute โดยใช้ self. นำหน้า
    #สร้าง method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def showdetail(self):
        print(f"ชื่อพนักงาน {self.name} เงินเดือน {self.salary} แผนก {self.department}")

emp1 = Employee()
emp1.detail("กร",30000,"โปรแกรมเมอร์") # name -> กร salary -> 30000
emp1.showdetail()

emp2 = Employee()
emp2.detail("โบว์",50000,"บัญชี") # name -> โบว์ salary -> 30000
emp2.showdetail()

emp3 = Employee()
emp3.detail("หนมน้า",10000,"CEO") # name -> หนมน้า salary -> 30000
emp3.showdetail()
