#!/usr/bin/python3
import subprocess
from sys import argv


def shell_output(cmd):
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
    return result


if len(argv) > 1:
    if argv[1] == 'start':
        subprocess.Popen(['dropbox', 'start'])
    elif argv[1] == 'stop':
        subprocess.Popen(['dropbox', 'stop'])

status = shell_output(['dropbox', 'status'])
status = status.replace('Dropbox ', '')

if 'sync' in status.lower():
    status = 'Syncing'

print(' {0}'.format(status))
