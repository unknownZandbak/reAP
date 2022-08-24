from employee import Employee
from shelf import Shelf

class Warehouse:
    
    def __init__(self, employees :list[Employee] = [], shelves :list[Shelf] = []) -> None:
        self.employees = employees
        self.shelves = shelves

    def getEmployees(self) -> list[Employee]:
        return self.employees

    def getShelves(self) -> list[Shelf]:
        return self.shelves

    def addEmployee(self, employee:Employee) -> None:
        self.employees.append(employee)

    def removeEmployee(self, employee:Employee) -> None:
        self.employees.remove(employee)

    def addShelf(self, shelf:Shelf) -> None:
        self.employees.append(shelf)
    
    def removeShelf(self, shelf:Shelf) -> None:
        self.shelves.remove(shelf)

    def rearrangeShelf(self, shelf:Shelf) -> bool:
        pass

    def pickItems(self, itenName:str, itemCount:int) -> bool:
        pass

    