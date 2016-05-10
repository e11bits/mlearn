#!/usr/bin/python3

import os

if __name__ == '__main__':

    # This will make sure that the octaverc user startup file will contain
    # a line to set the graphics toolkit to gnuplut.  It might add multiple
    # lines, but this shouldn't hurt.

    startup_path = os.path.expanduser('~/.octaverc')
    option = 'graphics_toolkit'
    value = 'gnuplot'

    with open(startup_path, 'a') as startup_file:
            startup_file.write(option + ' ' + value + '\n')
