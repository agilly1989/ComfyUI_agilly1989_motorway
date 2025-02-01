
from .ramps.generated import NODE_CLASS_MAPPINGS as GeneratedMapping
from .util_nodes.primitives import NODE_CLASS_MAPPINGS as PrimitiveMapping

NODE_CLASS_MAPPINGS = GeneratedMapping
NODE_CLASS_MAPPINGS.update(PrimitiveMapping)