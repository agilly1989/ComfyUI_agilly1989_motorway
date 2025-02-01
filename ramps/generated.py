import itertools
import string

from ..custom_types import CustomIO, MotorwayClass
from comfy.comfy_types import IO

MAX_IN = 10
MAX_OUT = 10

# Helper function to get character labels
def get_char(idx):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return chars[idx % len(chars)]  # Wrap around if index exceeds length

# Generate output types and names
def generate_outputs(count):
    return (
        (CustomIO.MOTORWAY,) + (IO.ANY,) * count,
        (CustomIO.MOTORWAY.name,) + tuple(f"{IO.ANY.name} ({get_char(x)})" for x in range(count))
    )

# Generate input types
def generate_inputs(in_count, out_count):
    max_count = max(in_count, out_count)
    return classmethod(lambda cls: {
        "required": {"MOTORWAY": (CustomIO.MOTORWAY,)},
        "optional": {
            **{f"{IO.ANY.name}_({get_char(x)})": (IO.ANY,) for x in range(in_count)},
            **{f"{IO.ANY.name}_({get_char(x)})_key": (IO.STRING,) for x in range(max_count)}
        }
    })

# Function logic for processing nodes
def node_function(self, MOTORWAY: MotorwayClass, **kwargs):
    node_connections = [key for key in kwargs if "key" not in key]
    connection_keys = [key for key in kwargs if "key" in key]

    # Process inputs
    for connection in node_connections:
        key_value = kwargs.get(f"{connection}_key")
        if key_value not in (None, ""):
            #MOTORWAY[key_value] = kwargs.get(connection)
            MOTORWAY.update(key_value,kwargs.get(connection))

    # Process outputs
    outputs = [MOTORWAY]
    for connection_key in connection_keys:
        key_value = kwargs.get(connection_key)
        if key_value not in (None, ""):
            outputs.append(MOTORWAY.get(key_value))

    return tuple(outputs)


# Dictionary for node mappings
NODE_CLASS_MAPPINGS = {}

# Generate all possible Motorway nodes
def create_motorway_nodes():
    for in_count, out_count in itertools.product(range(MAX_IN + 1), range(MAX_OUT + 1)):
        if in_count == 0 and out_count == 0:
            continue
        return_types, return_names = generate_outputs(out_count)
        node_name = f"Motorway {in_count}x{out_count}"
        
        new_node = type(
            f"Motorway{in_count}x{out_count}",
            (),
            {
                "INPUT_TYPES": generate_inputs(in_count, out_count),
                "RETURN_TYPES": return_types,
                "RETURN_NAMES": return_names,
                "IGNORE_MOTORWAY": True,
                "FUNCTION": "function",
                "CATEGORY": f"agilly1989 Nodes/Motorways",
                "NODE_NAME": node_name,
                "function": node_function,
            }
        )
        NODE_CLASS_MAPPINGS[node_name] = new_node

# Define MotorwayStart class
class MotorwayStart:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}
    
    RETURN_TYPES = (CustomIO.MOTORWAY,)
    FUNCTION = "function"
    CATEGORY = "agilly1989 Nodes/Motorway Start"
    
    def function(self):
        return (MotorwayClass(),)

# Create and register nodes
create_motorway_nodes()
NODE_CLASS_MAPPINGS["MotorwayStart"] = MotorwayStart
