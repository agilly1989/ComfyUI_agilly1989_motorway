from comfy.comfy_types import IO
from ..custom_types import CustomIO

class MotorwaySeed:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"seed":(IO.INT,{"default":0,"min":0,"max":0xffffffff})},
                "optional": {"MOTORWAY":(CustomIO.MOTORWAY,{"tooltip":"Optional Input. If not connected will act as a \"Motorway Start\" node"}),
                             "key":(IO.STRING,{"default":"seed"})}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,IO.INT)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Utilities/Seed"
    
    def function(self,MOTORWAY:dict={},seed:int=0,key:str="seed"):
        MOTORWAY.update({key:seed})
        return (MOTORWAY,seed)
    
NODE_CLASS_MAPPINGS = {"MotorwaySeed":MotorwaySeed}