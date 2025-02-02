import nodes
from pathlib import Path
from comfy.comfy_types import ComfyNodeABC, IO, InputTypeDict
from comfy_execution.graph_utils import GraphBuilder
from ..custom_types import CustomIO, MotorwayClass

def nodeOutputs(node: ComfyNodeABC):
    RETURN_TYPES = []
    RETURN_NAMES = []
    
    if hasattr(node, "RETURN_TYPES"):
        RETURN_TYPES = [f"{x}" for x in node.RETURN_TYPES]
        RETURN_NAMES = RETURN_TYPES
    
    if hasattr(node, "RETURN_NAMES"):
        RETURN_NAMES = [f"{x}" for x in node.RETURN_NAMES]

    pairs = zip(RETURN_TYPES, RETURN_NAMES)
    outputDict = {f'OUTPUT_{returnName}_key': (IO.STRING, {"default": returnName}) for returnType, returnName in pairs}

    return outputDict

def nodeInputs(node: ComfyNodeABC):
    
    INPUT_TYPES:InputTypeDict = node.INPUT_TYPES()

    widgetInputs = []
    convert2key = []

    mainDict = {'required':{},'optional':{},'hidden':{}}
    
    for inputRequirement,inputDict in INPUT_TYPES.items():
        if inputRequirement != 'hidden':
            for kwargname,inputTuple in inputDict.items():
                inputType = inputTuple[0]

                if len(inputTuple) > 1:
                    inputData = inputTuple[1]
                else:
                    inputData = {}

                if inputType in IO.PRIMITIVE.split(',') or isinstance(inputType,list):
                    widgetInputs.append({kwargname:inputTuple})
                else:
                    convert2key.append({f'INPUT_{kwargname}_key':(IO.STRING,{'default':kwargname})})

        else: 
            mainDict['hidden'].update(inputDict)
    
    if len(convert2key) != 0:
        mainDict['required'].update({CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,)})
        for x in convert2key:
            mainDict['required'].update(x)
    else:
        mainDict['optional'].update({CustomIO.MOTORWAY.value:(CustomIO.MOTORWAY,)})

    for x in widgetInputs:
        mainDict['required'].update(x)

    return mainDict

def genInputs(node):
    baseDict = nodeInputs(node)
    baseDict['required'].update(nodeOutputs(node))
    return baseDict

class BaseClass(ComfyNodeABC):
    EXPERIMENTAL = True
    FUNCTION = "basefunction"
    RETURN_TYPES = (CustomIO.MOTORWAY,)
    CLONED_NODE = None
    CATEGORY = "agilly1989 Nodes/Motorway-ed"

    @classmethod
    def INPUT_TYPES(cls):
        return genInputs(cls.CLONED_NODE[1])

    def basefunction(self, **kwargs):
        MOTORWAY:MotorwayClass = kwargs.pop(CustomIO.MOTORWAY)
        workingNode:ComfyNodeABC = self.CLONED_NODE[1]()
        def getInputName(data:str):
            data = data.replace("INPUT_",'').replace("OUTPUT_",'').replace("_key",'')
            return data

        #work out input args
        nodeInputKwargs = {}
        nodeOutputsKwargs = {}
        nodeWidgetKwargs = {}

        for widgetName,widgetKey in kwargs.items():
            if widgetName.startswith("INPUT"):
                nodeInputKwargs.update({getInputName(widgetName):MOTORWAY.get(widgetKey)})
            elif widgetName.startswith("OUTPUT"):
                nodeOutputsKwargs.update({getInputName(widgetName):widgetKey})
            else:
                nodeWidgetKwargs.update({widgetName:widgetKey})

        outData = getattr(workingNode,workingNode.FUNCTION)(**{**nodeInputKwargs,**nodeWidgetKwargs})
        
        position = 0
        for widgetName,widgetKey in nodeOutputsKwargs.items():
            MOTORWAY.update(widgetKey,outData[position])
            position += 1

        return (MOTORWAY,)

# Dictionary to store dynamically created classes
NODE_CLASS_MAPPING = {}

for nodeName, nodeClass in nodes.NODE_CLASS_MAPPINGS.items():
    newNodeName = f"{nodeName}_motorway_edition"
    new_class = type(
        newNodeName,
        (BaseClass,),
        {
            "CATEGORY": f"{BaseClass.CATEGORY}/{nodeClass.CATEGORY}",
            "CLONED_NODE": (nodeName, nodeClass),  # Fixed the lambda
        }
    )
    NODE_CLASS_MAPPING[newNodeName] = new_class  # Store in the dictionary

