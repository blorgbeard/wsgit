#!/usr/bin/python3

""" wsgit
"""
import os
from operator import itemgetter

import colorama
from colorama import Fore

import git
import log
import workspace

colorama.init()


def show_branch_matrix(cwd=".", master_branches=("master",)):
    """ Show matrix of repositories and branches. """
    repos = [os.path.basename(p) for p in workspace.repository_paths(cwd)]
    repo_branches = [{
        "repo": repo,
        "branches": git.branches(repo)
        } for repo in repos]

    non_unique_branch_names = (
        b.name
        for rb in repo_branches
        for b in rb['branches'].values()
        if not b.name in master_branches)

    branch_counts = {}
    for name in non_unique_branch_names:
        if name in branch_counts:
            branch_counts[name] += 1
        else:
            branch_counts[name] = 1

    # sort branches by:
    #  1. master(s) first
    #  2. most packages have it
    #  3. alphabetically

    branch_counts = list(branch_counts.items())
    branch_counts.sort(key=itemgetter(0))
    branch_counts.sort(key=itemgetter(1), reverse=True)
    sorted_branch_names = [branch[0] for branch in branch_counts]
    sorted_branch_names = list(master_branches) + sorted_branch_names

    max_repo_name_length = max(len(os.path.basename(rb["repo"]))
                               for rb in repo_branches)
    for data in repo_branches:
        repo_name = data["repo"]
        repo_padding = max_repo_name_length - len(repo_name)
        repo_branches = data["branches"]
        line = repo_name + (" " * repo_padding)
        for branch_name in sorted_branch_names:
            if branch_name in repo_branches:
                if repo_branches[branch_name].current:
                    line += "  * " + Fore.GREEN + branch_name + Fore.RESET
                else:
                    line += "    " + branch_name
            else:
                line += "    " + (" " * len(branch_name))
        print(line)

if __name__ == "__main__":
    # todo: parse args
    log.set_level('warn')
    show_branch_matrix()
