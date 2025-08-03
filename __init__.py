
from .ramps.generated import NODE_CLASS_MAPPINGS as GeneratedMapping
from .util_nodes.primitives import NODE_CLASS_MAPPINGS as PrimitiveMapping
#from .clone_nodes_in_the_dangerzone.nodes import NODE_CLASS_MAPPING as ClonedNodeMapping
NODE_CLASS_MAPPINGS = {}
#NODE_CLASS_MAPPINGS.update(ClonedNodeMapping)
NODE_CLASS_MAPPINGS.update(GeneratedMapping)
NODE_CLASS_MAPPINGS.update(PrimitiveMapping)