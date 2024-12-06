from employee import Employee
from accounting import Accounting
from sale import Sale
from programmer import Programmer
accounting = Accounting("kon",15000,26)
accounting._showdetail()

programmer = Programmer("นัท",30000,0,"pytorch")
programmer._showdetail()

sale = Sale("โบว์วี่",20000,"บางปะกง")
sale._showdetail()
