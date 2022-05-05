#!/usr/bin/env python3


from typing import Union

import numpy as np
from numpy.typing import NDArray
from pydantic import validate_arguments

from ramanchada2.misc.spectrum_deco import spectrum_algorithm_deco
from ..spectrum import Spectrum


@spectrum_algorithm_deco
@validate_arguments(config=dict(arbitrary_types_allowed=True))
def __truediv__(
        old_spe: Spectrum,
        new_spe: Spectrum,
        arg: Union[Spectrum, NDArray, float]):
    if isinstance(arg, Spectrum):
        if not (old_spe.x == arg.x).all():
            ValueError('x axes should be equal')
        new_spe.y = old_spe.y / arg.y
    elif isinstance(arg, np.ndarray):
        if old_spe.y.shape != arg.shape:
            ValueError(f'shapes does not match {old_spe.y.shape} != {arg.shape}')
        new_spe.y = old_spe.y / arg
    elif isinstance(arg, float):
        new_spe.y = old_spe.y / arg
    else:
        ValueError('This should never happen')
