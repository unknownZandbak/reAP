from employee import Employee
from shelf import Shelf, Pallet

class Warehouse:
    
    def __init__(self, employees :list[Employee] = [], shelves :list[Shelf] = []) -> None:
        self.employees = employees
        self.shelves = shelves

    def __repr__(self) -> str:
        return str(f"\nEmployees: {len(self.employees)}\nShelves: {len(self.shelves)}\n\n======Employees======\n{self.employees}\n\n======Shelfs======\n{repr(self.shelves)}\n")

    def getEmployees(self) -> list[Employee]:
        return self.employees

    def getShelves(self) -> list[Shelf]:
        return self.shelves

    def addEmployee(self, employee:Employee) -> None:
        self.employees.append(employee)

    def removeEmployee(self, employee:Employee) -> None:
        self.employees.remove(employee)

    def addShelf(self, shelf:Shelf) -> None:
        self.shelves.append(shelf)
    
    def removeShelf(self, shelf:Shelf) -> None:
        self.shelves.remove(shelf)

    def rearrangeShelf(self, shelf:Shelf, employee:Employee) -> bool:
        print("\nRearranging ===")
        if employee.busy or not employee.forkliftCertificate:
            print("Rearranging failed: employee busy or not qualified")
            return False
            
        employee.busy = True
        shelf.pallets = sorted(shelf.pallets, key=lambda pallet: pallet.itemCount)
        employee.busy = False
        print("Done ==========")
        return True

    def pickItems(self, itemName:str, itemCount:int) -> bool:
        total_count = 0
        found_pallets:list[Pallet] = []
        for shelf in self.shelves:
            for pallet in shelf.pallets:
                try:
                    if pallet.itemName.lower() == itemName.lower():
                        total_count += pallet.itemCount
                        found_pallets.append(pallet)
                except AttributeError:
                    continue

        if total_count >= itemCount:
            for pallet in found_pallets:
                if pallet.itemCount > itemCount:
                    pallet.itemCount = pallet.itemCount - itemCount  
                else:
                    itemCount -= pallet.itemCount
                    pallet.itemCount = 0 
        else:
            return False

        return True

    