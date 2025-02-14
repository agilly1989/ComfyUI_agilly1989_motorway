from __future__ import annotations
from enum import Enum
import hashlib

class CustomIO(str,Enum):
    MOTORWAY = "MOTORWAY 🚌💨"

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

    def varNameToHash(self,varName:str):
        varNameHash = hashlib.sha256(varName.encode()).hexdigest()
        return f"hash_{varNameHash}"

    def update(self,varName:str,varData):
        setattr(self,self.varNameToHash(varName),varData)

    def get(self, varName: str):
        try:
            return getattr(self, self.varNameToHash(varName))
        except AttributeError:
            raise KeyError(f"Key: `{varName}` doesn't exist in motorway")

    def asDict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if key.startswith("hash_")
        }

    def clone(self):
        new_instance = MotorwayClass()
        for key, value in self.asDict().items():
            setattr(new_instance, key, value)  # Copy only `hash_` attributes
        return new_instance
    
CustomIO.MOTORWAY.value