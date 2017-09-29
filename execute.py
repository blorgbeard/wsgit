import log
import subprocess

def run(*args):
    log.debug('running {command}', command=args)
    return subprocess.check_output(args, universal_newlines=True)
