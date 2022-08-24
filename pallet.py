class Pallet:
    
    def __init__(self, itemName:str, itemCount:int, itemCapacity:int) -> None:
        self.itemName = itemName
        self.itemCount = itemCount
        self.itemCapacity = itemCapacity

    def getItemName(self) -> str:
        return self.itemName
    
    def getItemCount(self) -> int:
        return self.itemCount

    def getRemainingSpace(self) -> int:
        return self.itemCapacity - self.itemCount

    def reallocateEmptyPallet(self, itemName:str, itemCapacity:int) -> bool:
        if self.itemCount <= 0:
            return False

        self.itemName = itemName
        self.itemCapacity = itemCapacity
        return True
    
    def takeOne(self) -> bool:
        if self.itemCount <= 0:
            return False
        
        self.itemCount -= 1
        return True

    def putOne(self) -> bool:
        if self.itemCount >= self.itemCapacity:
            return False
        
        self.itemCount += 1
        return True
