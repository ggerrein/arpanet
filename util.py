import importlib
import sys

# this function parses the command line arguments into a dictionary
def get_key_vals():
    key_vals = {}
        key, val = arg.split('=')
        key_vals[key] = val
    return key_vals

# this function returns the application object
def get_app():
    module = importlib.import_module(f"my_apps.{get_key_vals()['app']}")
    my_func = getattr(module, 'get_app')
    return my_func

# this function returns a list of agents/tools
def get_agents():
    tools = []
    tool_list = list(get_key_vals()['agents'].split(','))
    for arg in tool_list:
        module = importlib.import_module(f'my_agents.{arg}')
        my_func = getattr(module, 'get_tool')
        tools.append(my_func())
    return tools
