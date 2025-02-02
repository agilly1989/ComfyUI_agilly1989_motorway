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
    
    def function(self,**kwargs):
        MOTORWAY = kwargs.get(CustomIO.MOTORWAY.value,None)
        key = kwargs.get("key",self.INPUT_TYPES()['optional']['key'][1]['default'])
        seed = kwargs.get("seed",self.INPUT_TYPES()['required']['seed'][1]['default'])

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
    
    def function(self,**kwargs):
        MOTORWAY = kwargs.get(CustomIO.MOTORWAY.value,None)
        key = kwargs.get("key",self.INPUT_TYPES()['optional']['key'][1]['default'])
        INT = kwargs.get("INT",self.INPUT_TYPES()['required']['INT'][1]['default'])

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
    
    def function(self,**kwargs):
        MOTORWAY = kwargs.get(CustomIO.MOTORWAY.value,None)
        key = kwargs.get("key",self.INPUT_TYPES()['optional']['key'][1]['default'])
        FLOAT = kwargs.get("FLOAT",self.INPUT_TYPES()['required']['FLOAT'][1]['default'])

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

    def function(self,**kwargs):
        MOTORWAY = kwargs.get(CustomIO.MOTORWAY.value,None)
        key = kwargs.get("key",self.INPUT_TYPES()['optional']['key'][1]['default'])
        STRING = kwargs.get("STRING",self.INPUT_TYPES()['required']['STRING'][1]['default'])

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
    
    def function(self,**kwargs):
        MOTORWAY = kwargs.get(CustomIO.MOTORWAY.value,None)
        key = kwargs.get("key",self.INPUT_TYPES()['optional']['key'][1]['default'])
        STRING = kwargs.get("STRING",self.INPUT_TYPES()['required']['STRING'][1]['default'])

        if MOTORWAY == None:
            MOTORWAY = MotorwayClass()
        MOTORWAY.update(key,STRING)
        return (MOTORWAY,STRING)

NODE_CLASS_MAPPINGS = {"MotorwaySeed":MotorwaySeed,
                       "MotorwayInt":MotorwayInt,
                       "MotorwayFloat":MotorwayFloat,
                       "MotorwayStr":MotorwayStr,
                       "MotorwayStrMulti":MotorwayStrMulti}