"""Script to filter an image """
import sys
from psyfilter import psyfilter

if __name__ == '__main__':
    args = sys.argv
    usage = 'Usage: pypsy <src> <dest>'

    if len(args) > 2:
        raise Exception(usage)

    imagefile = args[0]
    pass
