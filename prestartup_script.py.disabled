from unittest.mock import patch as unittestPatch
import nodes
import os
from pathlib import Path

# Backup original functions
original_listdir = os.listdir
original_init_external_custom_nodes = nodes.init_external_custom_nodes

def patched_init_external_custom_nodes():
    """ Wrapper to patch os.listdir only inside init_external_custom_nodes. """
    def sorted_listdir(path):
        original_list = sorted(original_listdir(path))  # Sort all modules first
        if Path(__file__).parts[-2] in original_list:
            original_list.append(original_list.pop(original_list.index(Path(__file__).parts[-2])))
        return original_list  

    with unittestPatch("os.listdir", new=sorted_listdir):
        original_init_external_custom_nodes()  # Call the function with patched behavior

# Now overwrite the original function
nodes.init_external_custom_nodes = patched_init_external_custom_nodes
