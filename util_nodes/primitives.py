from comfy.comfy_types import IO
from ..custom_types import CustomIO, MotorwayClass

class MotorwaySeed:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"seed":(IO.INT,{"default":0,"min":0,"max":0xffffffffffffffff})},
                "optional": {CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"seed"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.INT)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Primitives/Numbers"
    
    def function(self,MOTORWAY=None,seed:int=0,key:str="seed"):
        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,seed)

        return (MOTORWAY,seed)

class MotorwayInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"INT":(IO.INT,{"default":0})},
                "optional": {CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"integer"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.INT)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Primitives/Numbers"
    
    def function(self,MOTORWAY=None,INT:int=0,key:str="integer"):
        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,INT)
        return (MOTORWAY,INT)

class MotorwayFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"FLOAT":(IO.FLOAT,{"default":0,"step":0.001})},
                "optional": {CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"float"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.FLOAT)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Primitives/Numbers"
    
    def function(self,MOTORWAY=None,FLOAT:int=0,key:str="float"):
        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,FLOAT)
        return (MOTORWAY,FLOAT)

class MotorwayStr:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"STRING":(IO.STRING,{"default":""})},
                "optional": {CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"string"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.STRING)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Primitives/Strings"

    def function(self,MOTORWAY=None,STRING:int=0,key:str="string"):
        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,STRING)
        return (MOTORWAY,STRING)

class MotorwayStrMulti:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"STRING":(IO.STRING,{"default":"","multiline":True})},
                "optional": {CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"string"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.STRING)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Primitives/Strings"
    
    def function(self,MOTORWAY=None,STRING:int=0,key:str="string"):
        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,STRING)
        return (MOTORWAY,STRING)

NODE_CLASS_MAPPINGS = {"MotorwaySeed":MotorwaySeed,
                       "MotorwayInt":MotorwayInt,
                       "MotorwayFloat":MotorwayFloat,
                       "MotorwayStr":MotorwayStr,
                       "MotorwayStrMulti":MotorwayStrMulti}