"""Useful tools for fMRI analysis"""

__version__ = '0.1'

from . import hrf
from . import design
from . import stats
from .io import read_gifti
from .nuisance import (legendre)