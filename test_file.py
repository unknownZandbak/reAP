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
    
    # Shelves
    s1 = Shelf()
    s2 = Shelf()
    s3 = Shelf()

    def test_add_employee(self):

        self.w1.addEmployee(self.e1)
        self.w1.addEmployee(self.e3)
        self.w1.addEmployee(self.e4)

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
        self.fail("No testing code")

    def test_rearrange_shelves(self):
        self.fail("No testing code")

    def test_pick_items(self):
        self.fail("No testing code")

class TestShelf(TestCase):
    
    def test_get_slot_status(self):
        self.fail("No testing code")
    
    def test_remove_pallet(self):
        self.fail("No testing code")

    def test_insert_pallet(self):
        self.fail("No testing code")

class TestPallet(TestCase):

    def test_get_remaining_space(self):
        self.fail("No testing code")

    def test_reallocate_empty_pallet(self):
        self.fail("No testing code")

    def test_take_one(self):
        self.fail("No testing code")

    def test_put_one(self):
        self.fail("No testing code")

if __name__ == '__main__' :
    main()