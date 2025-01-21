#!/usr/bin/env python

# above is the shebang line which tells the interpreter to run as a script

import fire
from mylib.logic import wiki

# This line tells the python interpreter only run this code if its run as a script
if __name__ == "__main__":
    fire.Fire(wiki)
