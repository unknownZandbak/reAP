class Employee:
    
    def __init__(self, name:str, forkliftCertificate:bool) -> None:
        self.NAME = name
        self.busy = False
        self.forkliftCertificate = forkliftCertificate

    def __repr__(self) -> str:
        return str(f"\nName:\t{self.NAME} \nBusy:\t{self.busy} \nForkliftcertified: \t{self.forkliftCertificate}")

    def getName(self) -> str:
        return self.NAME

    def getBusy(self) -> bool:
        return self.busy
    
    def getforkliftCertificate(self) -> bool:
        return self.forkliftCertificate

    def setBusy(self, newState:bool) -> None:
        self.busy = newState

    def setforkliftCertificate(self, newState:bool) -> None:
        self.forkliftCertificate = newState
