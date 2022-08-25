import numpy as np
from pallet import Pallet

class Shelf:
    
    MAX_PALLETS = 4
            
    def __init__(self) -> None:
        self.pallets: list[Pallet] = [Pallet() for x in range(self.MAX_PALLETS)]
    
    def __repr__(self) -> str:
        result = f"\nShelf ID:\t{id(self)}"
        for pallet in self.pallets:
            result += f"\n----\nItem Name:\t{pallet.itemName}\nItem Count:\t{pallet.itemCount}\nCapacity:\t{pallet.itemCapacity}"
        return  result

    def getSlotStatus(self) -> list[bool]:
        np_slots = np.asanyarray(self.pallets)
        slotStatus = np_slots != 0
        return list(slotStatus)
    
    def removePallet(self, slot:int) -> bool:
        if type(self.pallets[slot]) != Pallet:
            return False

        self.pallets[slot] = 0
        return True     

    def insertPallet(self, slot:int, pallet:Pallet) -> bool:
        if type(self.pallets[slot]) == Pallet:
            return False

        self.pallets[slot] = pallet
        return True
