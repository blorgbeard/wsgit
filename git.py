""" git-related functions """

import os
import execute

def is_git_repository(repo_path):
    """ Return a boolean indicating whether the given path is a git repository root. """
    return os.path.isdir(os.path.join(repo_path, '.git'))

def git(repo_path, command, *args):
    """ Execute a git command and return the result as a string """
    return execute.run("git", "-C", repo_path, command, *args)

class Branch:
    """ Represents a git branch in a particular repository. """
    def __init__(self, name, current=False):
        self.name = name
        self.current = current

def branches(repo_path):
    """ Return a list of local branches in the given repo """
    lines = git(repo_path, 'branch', '--list', '--color=never').splitlines()
    splut = [(line[:2], line[2:]) for line in lines]
    return {line[1]: Branch(line[1], line[0] == "* ") for line in splut}
