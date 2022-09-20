""" PyLabTools v0.6 Configuration Template.

This module provides a template for configuring custom experiment control software for version 0.6 of PyLabTools.
Sam Condon, 2022-09-20
"""
from . import hw
from . import control
from . import measure
from . import instruments
from . import procedures

# - Populate these lists with configuration dictionaries defined in the imported files! - #
VIEWERS = []
RECORDERS = []
PROCEDURES = []
CONTROLLERS = []
INSTRUMENT_SUITE = []
