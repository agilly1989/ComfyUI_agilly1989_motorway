from enum import Enum

class CustomIO(str,Enum):
    MOTORWAY = "MOTORWAY"

    def __str__(self) -> str:
        return self.value
    
    def __ne__(self, value: object) -> bool:
        if self == "*" or value == "*":
            return False
        if not isinstance(value, str):
            return True
        a = frozenset(self.split(","))
        b = frozenset(value.split(","))
        return not (b.issubset(a) or a.issubset(b))
    

class MotorwayClass:
    def __init__(self):
        pass

    def update(self,varName,varData):
        setattr(self,varName,varData)

    def get(self,varName):
        return getattr(self,varName)