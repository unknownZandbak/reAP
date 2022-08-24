import numpy as np
from pallet import Pallet

class Shelf:
    
    MAX_PALLETS = 4
            
    def __init__(self) -> None:
        self.slots: list[Pallet] = [Pallet]*4

    def getSlotStatus(self) -> list[bool]:
        slotStatus = self.slots != 0
        return slotStatus
    
    def removePallet(self, slot:int) -> bool:
        if type(self.slots[slot]) != Pallet:
            return False

        self.slots[slot] = 0
        return True     

    def insertPallet(self, slot:int, pallet:Pallet) -> bool:
        if type(self.slots[slot]) == Pallet:
            return False

        self.slots[slot] = pallet
        return True
