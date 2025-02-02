from unittest.mock import patch as unittestPatch
import nodes
import os

# Backup original functions
original_listdir = os.listdir
original_init_external_custom_nodes = nodes.init_external_custom_nodes

def patched_init_external_custom_nodes():
    """ Wrapper to patch os.listdir only inside init_external_custom_nodes. """
    def sorted_listdir(path):
        original_list = sorted(original_listdir(path))  # Sort all modules first
        if "Comfyui_agilly_motorway" in original_list:
            # Move "Comfyui_agilly_motorway" to the end of the list
            original_list.append(original_list.pop(original_list.index("ComfyUI_agilly1989_motorway")))
        return original_list  

    with unittestPatch("os.listdir", new=sorted_listdir):
        original_init_external_custom_nodes()  # Call the function with patched behavior

# Now overwrite the original function
nodes.init_external_custom_nodes = patched_init_external_custom_nodes
