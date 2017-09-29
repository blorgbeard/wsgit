""" Detection of "workspace" (common parent folder) """

import os
from git import is_git_repository

def is_workspace_root(path):
    """ A workspace is just the parent folder of at least one git repository root folder. """
    for child in os.listdir(path):
        if os.path.isdir(child) and is_git_repository(child):
            return True
    return False

def find_workspace_root(search_from="."):
    """ Search upwards for a workspace folder """
    search_from = os.path.abspath(search_from)
    current = search_from
    while True:
        if is_workspace_root(current):
            return current
        if os.path.ismount(current):
            message = "The folder {start} doesn't seem to be in a workspace"
            raise Exception(message.format(start=search_from))
        current = os.path.abspath(os.path.join(current, ".."))

def repository_paths(somewhere_in_workspace="."):
    """ Get a list of package paths in the workspace. """
    root = find_workspace_root(somewhere_in_workspace)
    children = (os.path.join(root, t) for t in os.listdir(root))
    return [t for t in children if os.path.isdir(t) and is_git_repository(t)]
