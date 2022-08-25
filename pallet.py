class Pallet:
    
    def __init__(self, itemName:str|None = None, itemCount:int = 0) -> None:
        self.itemName = itemName
        self.itemCount = itemCount
        self.itemCapacity = itemCount

    def __repr__(self) -> str:
        return str(f"\nItem Name:\t{self.itemName}\nItem Count:\t{self.itemCount}\nCapacity:\t{self.itemCapacity}")

    def getItemName(self) -> str:
        return self.itemName
    
    def getItemCount(self) -> int:
        return self.itemCount

    def getRemainingSpace(self) -> int:
        return self.itemCapacity - self.itemCount

    def reallocateEmptyPallet(self, itemName:str, itemCapacity:int) -> bool:
        if self.itemCount > 0:
            return False

        self.itemName = itemName
        self.itemCount = itemCapacity
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
