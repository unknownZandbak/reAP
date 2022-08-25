from warehouse import *
from unittest import TestCase, main

class TestWarehouse(TestCase):
    
    # Setup Warehouse
    w1 = Warehouse()

    #  ̶S̶l̶a̶v̶e̶s̶ Employees
    e1 = Employee("james", 0)
    e2 = Employee("'Tom'", 1)
    e3 = Employee("'Shane'", 1)
    e4 = Employee("'Carol'", 0)

    w1.addEmployee(e1)
    w1.addEmployee(e3)
    w1.addEmployee(e4)
    
    # Shelves
    s1 = Shelf()
    s2 = Shelf()
    s3 = Shelf()

    w1.addShelf(s1)
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
    

    def test_add_employee(self):

        self.assertIn(self.e1, self.w1.employees)
        self.assertNotIn(self.e2, self.w1.employees)
        self.assertIn(self.e3, self.w1.employees)
        self.assertIn(self.e4, self.w1.employees)

    def test_remove_employee(self):

        self.w1.removeEmployee(self.e3)

        self.assertIn(self.e1, self.w1.employees)
        self.assertNotIn(self.e2, self.w1.employees)
        self.assertNotIn(self.e3, self.w1.employees)
        self.assertIn(self.e4, self.w1.employees)
    
    def test_add_shelf(self):

        self.assertIn(self.s1, self.w1.shelves)
        self.assertNotIn(self.s2, self.w1.shelves)
        self.assertIn(self.s3, self.w1.shelves)

    def test_remove_shelf(self):
        
        self.w1.removeShelf(self.s1)

        self.assertNotIn(self.s1, self.w1.shelves)
        self.assertNotIn(self.s2, self.w1.shelves)
        self.assertIn(self.s3, self.w1.shelves)

    def test_rearrange_shelves(self):
        self.assertTrue(self.w1.rearrangeShelf(self.s2, self.e2))
        self.assertFalse(self.w1.rearrangeShelf(self.s2, self.e1))

    def test_pick_items(self):
        
        self.w1.pickItems("TV's", 16)
        self.assertEqual(self.s1.pallets[0].itemCount, 0)
        self.assertEqual(self.s3.pallets[2].itemCount, 4)

class TestShelf(TestCase):

    # Setup of Shelves
    s1 = Shelf()
    s2 = Shelf()
    s3 = Shelf()

    s1.removePallet(0)
    s1.removePallet(2)

    s3.removePallet(3)

    def test_get_slot_status(self):
        self.assertEqual([False, True, False, True], self.s1.getSlotStatus())
        self.assertEqual([True, True, True, True], self.s2.getSlotStatus())
        self.assertEqual([True, True, True, False], self.s3.getSlotStatus())

    def test_remove_pallet(self):
        self.s2.removePallet(3)
        self.s3.removePallet(0)
        self.s3.removePallet(3)

        self.assertFalse(self.s1.pallets[0])
        self.assertFalse(self.s1.pallets[2])

        self.assertFalse(self.s2.pallets[3])

        self.assertFalse(self.s3.pallets[0])
        self.assertFalse(self.s3.pallets[3])


    def test_insert_pallet(self):
        
        p1 = Pallet("Ghost Costume's", 50)
        p2 = Pallet("Drone's", 48)

        self.s2.removePallet(3)

        self.s2.insertPallet(3, p1)
        self.s3.insertPallet(3, p2)

        self.assertIsInstance(self.s2.pallets[3], Pallet)
        self.assertIsInstance(self.s3.pallets[3], Pallet)

        self.assertEqual("Ghost Costume's", self.s2.pallets[3].getItemName())
        self.assertEqual("Drone's", self.s3.pallets[3].getItemName())

        self.assertEqual(50, self.s2.pallets[3].getItemCount())
        self.assertEqual(48, self.s3.pallets[3].getItemCount())

class TestPallet(TestCase):

    p1 = Pallet("Drone's", 40)
    p2 = Pallet("TV's", 56)
    p3 = Pallet("Couches", 12)
    p4 = Pallet("PC's", 23)

    for i in range(34):
        p1.takeOne()
    for i in range(14):
        p2.takeOne()
    for i in range(22):
        p3.takeOne()


    def test_get_remaining_space(self):
        self.assertEqual(34, self.p1.getRemainingSpace())
        self.assertEqual(14, self.p2.getRemainingSpace())
        self.assertEqual(12, self.p3.getRemainingSpace())
        self.assertEqual(0, self.p4.getRemainingSpace())

    def test_reallocate_empty_pallet(self):
        for i in range(34):
            self.p1.takeOne()
        self.p1.reallocateEmptyPallet("Bong's", 16)
        
        self.assertEqual("Bong's", self.p1.getItemName())
        self.assertEqual(16, self.p1.getItemCount())

        self.assertEqual("Couches", self.p3.getItemName())
        self.assertEqual(0, self.p3.getItemCount())

    def test_take_one(self):
        self.p1.takeOne()
        self.p2.takeOne()
        self.p3.takeOne()
        self.p4.takeOne()  

        self.assertEqual(15, self.p1.getItemCount())
        self.assertEqual(41, self.p2.getItemCount())
        self.assertEqual(0, self.p3.getItemCount())
        self.assertEqual(21, self.p4.getItemCount())

        self.p1.putOne()
        self.p2.putOne()
        self.p3.putOne()
        self.p4.putOne()

    def test_put_one(self):
        self.p1.putOne()
        self.p2.putOne()
        self.p3.putOne()
        self.p4.putOne()
        
        self.assertEqual(7, self.p1.getItemCount())
        self.assertEqual(43, self.p2.getItemCount())
        self.assertEqual(1, self.p3.getItemCount())
        self.assertEqual(23, self.p4.getItemCount())
        
        self.p1.takeOne()
        self.p2.takeOne()
        self.p3.takeOne()
        self.p4.takeOne()        

if __name__ == '__main__' :
    main()