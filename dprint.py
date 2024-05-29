import inspect
import os


def dprint(value):
    # get call
    frame = inspect.currentframe().f_back
    # get file and line
    absolute_filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    # get root
    project_root = os.getcwd()
    # get path
    relative_filename = os.path.relpath(absolute_filename, project_root)
    # get all variable in file
    local_vars = frame.f_locals

    # find var in indetnt id obj
    var_name = None
    for name, val in local_vars.items():
        if id(val) == id(value):
            var_name = name
            break

    if var_name:
        print(f">>>>>>>>>>>>> {var_name} = {value} {type(value)} ({relative_filename} : {lineno})")
    else:
        print(f">>>>>>>>>>>>> Value = {value} {type(value)} ({relative_filename} : {lineno})")


