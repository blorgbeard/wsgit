
__level_values = {
    'debug': 1,
#   'info': 2,      # if it's "info", it's the output of the command.
    'warn': 3,
#   'error': 4      # this is a cli app. if there's an error, we bail.
}
__current_level = __level_values['warn']

def set_level(level):
    global __current_level
    __current_level = __level_values[level]

def log(level, message, **kwargs):
    if __current_level > __level_values[level]:
        return
    print('[' + level + ']: ' + message.format(**kwargs))

def debug(message, **kwargs):
    log('debug', message, **kwargs)

def warn(message, **kwargs):
    log('warn', message, **kwargs)
