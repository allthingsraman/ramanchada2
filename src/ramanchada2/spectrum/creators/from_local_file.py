#!/usr/bin/env python3
"""Create spectrum from local files."""

from __future__ import annotations

from ..spectrum import Spectrum
from ramanchada2.misc.spectrum_constructor import spectrum_constructor_deco


@spectrum_constructor_deco
def from_local_file(spe: Spectrum, infile, filetype, **kwargs):
    """
    Read experimental spectrum from a local file.

    infile : file-like object
    filetype : str
        one of: txt...
    """
    if filetype in {'.jdx', '.dx'}:
        raise NotImplementedError('The implementation of JCAMP reader is missing')
    elif filetype in {'.txt', '.txtr', '.csv', '.prn', '.rruf'}:
        raise NotImplementedError('The implementation of TXT reader is missing')
    else:
        raise ValueError(f'filetype {filetype} not supported')
    # Vlues for spe.x, spe.y, spe.meta should be set here
