from __future__ import unicode_literals
import sys
import os
from subprocess import call
DEFAULT_CATALOGS = {
    'files': ['main.yml'],
    'handlers': ['main.yml'],
    'meta': ['main.yml'],
    'tasks': ['main.yml'],
    'templates': ['main.yml'],
    'vars': ['main.yml'],
    'defaults': ['main.yml'],
}

def main(role_name):
    if not os.path.exists(role_name):
        os.mkdir(role_name)

    for catalog, file_names in DEFAULT_CATALOGS.items():
        if not os.path.exists('{}/{}'.format(role_name, catalog)):
            os.mkdir('{}/{}'.format(role_name, catalog))
            for f_name in file_names:
                open('{}/{}/{}'.format(role_name, catalog, f_name), 'a').close()
    call(['tree',role_name])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('error: too few arguments')
    role_name = sys.argv[1]
    main(role_name) 
