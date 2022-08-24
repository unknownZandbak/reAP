from warehouse import *
from unittest import TestCase, main

class TestWarehouse(TestCase):

    def test_add_employee(self):
        self.fail("No testing code")

    def test_remove_employee(self):
        self.fail("No testing code")
    
    def test_add_shelf(self):
        self.fail("No testing code")

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