# What is this?

This my implemenation of a "pipe" in ComfyUI. Is it better or worse than others? No idea.

# Installation
Open your `ComfyUI/custom_nodes` folder and git clone this repository

# Usage
The node pattern is `Motorway [amount of inputs]x[amount of outputs]` so
* 1x5 would be 1 input and 5 outputs
* 0x3 would be 0 inputs and 5 outputs
* etc

Type in a key to identify what that input is and use it later down the "Motorway", Load the `Example.json` into ComfyUI to see what I mean.

You must start with the "MotorwayStart" node

# Behind the Scenes
The motorway is *literally* just a dict that gets passed on from node to node, so if you use an existing key later down the "Motorway" it will be overwritten

# Why Did I make this?
I didn't like how other "pipe" implementations were implemented.

# Compatibility

As far as I know, it should be compatible with all nodes, but if something breaks, tell me or "just don't use it"

# Will it break

Maybe, but "It works on my System"

# I want more inputs / outputs

If you go looking in `ramps/generated.py` you will see `MAX_IN` and `MAX_OUT`.. Enter whatever number you want (up to __52__)

# Feature Creep
* [ ] Motorway Merge (will probably be a "update A with B" thing because of `dicts`)
* [ ] Make it so it loads last and makes a clone of existing nodes so you don't need to add "Motorway" nodes
  * Will probably need patching of the node loading system to ensure that this loads last in the sequence, mega jank but will do the job