"""
AIfund 是基于 Python 的基金量化工具
"""

__version__ = "0.0.6"
__author__ = "yebaige"

import sys

if sys.version_info < (3, 7):
    print(f"AKShare {__version__} requires Python 3.7+ and 64 bit OS")
    sys.exit(1)

del sys

from aifund.fund_sou.fund_em import *
