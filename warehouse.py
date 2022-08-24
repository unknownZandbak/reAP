from employee import Employee
from shelf import Shelf

class Warehouse:
    
    def __init__(self, employees:list[Employee]|None, shelves:list[Shelf]|None) -> None:
        self.employees = employees
        self.shelves = shelves

    def addEmployee(self, employee:Employee) -> None:
        self.employees.append(employee)

    def addShelf(self, shelf:Shelf) -> None:
        self.employees.append(shelf)
    
    def rearrangeShelf(self, shelf:Shelf) -> bool:
        pass

    def pickItems(self, itenName:str, itemCount:int) -> bool:
        pass

    