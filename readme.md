# Installation
Open your ComfyUI/custom_nodes folder and git clone this repository

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

# Feature Creep
* [ ] Motorway Merge
* [ ] Make it so it loads last and makes a clone of existing nodes so you don't need to add "Motorway" nodes