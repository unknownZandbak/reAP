from warehouse import *

def setup_warehouse():
    w1 = Warehouse()

    #  ̶S̶l̶a̶v̶e̶s̶ Employees
    e1 = Employee("james", 0)
    e2 = Employee("'Tom'", 1)
    e3 = Employee("'Shane'", 1)
    e4 = Employee("'Carol'", 0)

    w1.addEmployee(e1)
    w1.addEmployee(e2)
    w1.addEmployee(e3)
    w1.addEmployee(e4)
    
    # Shelves
    s1 = Shelf()
    s2 = Shelf()
    s3 = Shelf()

    w1.addShelf(s1)
    w1.addShelf(s2)
    w1.addShelf(s3)

    # Pallets
    s1.pallets[0].reallocateEmptyPallet("TV's", 10)
    s1.pallets[1].reallocateEmptyPallet("PC's", 52)
    s1.pallets[3].reallocateEmptyPallet("Laptop's", 48)
    
    s2.pallets[0].reallocateEmptyPallet("TV's", 10)
    s2.pallets[1].reallocateEmptyPallet("Clothing", 108)
    s2.pallets[2].reallocateEmptyPallet("Printers", 6)
    s2.pallets[3].reallocateEmptyPallet("Laptop's", 48)
    
    s3.pallets[1].reallocateEmptyPallet("PC's", 52)
    s3.pallets[2].reallocateEmptyPallet("TV's", 10)
    s3.pallets[3].reallocateEmptyPallet("Laptop's", 48)

    return w1

def main():
    # een hele kleine demo van dat de code wel werkt en zo uigevoert kan worden.
    # je kan er zelf een soort van game loop van maken met cli commands om zo in realtime het warenhuis aantepassen.
    # maar door tijds gebrek doe ik dit nu niet, wel zijn alle methods en fuctions getest in de test file en werken ze naar behoren.

    w1 = setup_warehouse()

    print(w1)

    w1.pickItems("PC's", 16)
    w1.pickItems("Laptop's", 56)
    w1.pickItems("Clothing", 100)

    print(w1)

    w1.rearrangeShelf(w1.shelves[0])
    w1.rearrangeShelf(w1.shelves[1])
    w1.rearrangeShelf(w1.shelves[2])

    print(w1)


if __name__ == '__main__' :
    main()