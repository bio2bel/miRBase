# -*- coding: utf-8 -*-

"""Entrypoint module for Bio2BEL MirBase, in case you use `python -m bio2bel_mirbase`.
Why does this file exist, and why ``__main__``? For more info, read:
 - https://www.python.org/dev/peps/pep-0338/
 - https://docs.python.org/2/using/cmdline.html#cmdoption-m
 - https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from .cli import main

if __name__ == '__main__':
    main()
