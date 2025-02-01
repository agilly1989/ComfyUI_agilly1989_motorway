
from .ramps.generated import NODE_CLASS_MAPPINGS as GeneratedMapping
from .util_nodes.seed import NODE_CLASS_MAPPINGS as SeedMapping

NODE_CLASS_MAPPINGS = GeneratedMapping
NODE_CLASS_MAPPINGS.update(SeedMapping)