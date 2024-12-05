# การห่อหุ้ม Encapsulation -> ระดับการเข้าถึง
#Public = ใครๆก้ใช้งานได้ -> Facebook สาธาณะ
#Protected(_) = เข้าถึงได้เฉพาะคลาสตัวเองและลูก -> Post Facebook -> เพื่อน
#Private(__) = เฉพาะตัวเองที่เข้าถึงได้ -> Lock Post Facebook
#การสร้าง construtor คือ การกำหนดค่าเริ่มต้นให้กับวัตถุ
#ฟังชั่นเสริม
# class Employee:
#     def __init__(self,name,salary,department):
#         # Public attribute
#         self.name = name
#         self.salary = salary
#         self.department = department
#     # Public method
#     def showdetail(self):
#         print(f"ชื่อพนักงาน {self.name} เงินเดือน {self.salary} แผนก {self.department}")

# #Public
# obj1 = Employee(name="กร",
#                 salary=50000,
#                 department="CEO")
# obj1.salary = 70000
# obj1.showdetail()

#Protected(_)
# class Employee:
#     def __init__(self,name,salary,department):
#         # Protected attribute
#         self._name = name
#         self._salary = salary
#         self._department = department
#         # self._showdetail()
#     # Protected method
#     def _showdetail(self):
#         print(f"ชื่อพนักงาน {self._name} เงินเดือน {self._salary} แผนก {self._department}")
# obj1 = Employee(name="กร",
#                 salary=50000,
#                 department="CEO")
# #ถ้าเปลี่ยน attribute Public ค่าจะไม่เปลี่ยน
# obj1.name = "กรซ่า"
# obj1._showdetail()

#Private(__)
class Employee:
    def __init__(self,name,salary,department):
        # Private attribute
        self._name = name #Protected
        self.__salary = salary #Private
        self.__department = department #Private
        self.__showdetail()
    # Private method
    def __showdetail(self):
        print(f"ชื่อพนักงาน {self._name} เงินเดือน {self.__salary} แผนก {self.__department}")
obj1 = Employee(name="กร",
                salary=50000,
                department="CEO")
# obj1.__showdetail() # เรียกใช้งานไม่ได้ ต้องไปกำหนดใน class แทน
obj1._name = "กรซ่า"
obj1.__salary = 57000 #จะแก้ไขไม่ได้
obj1.__department = "Sale" #จะแก้ไขไม่ได้


