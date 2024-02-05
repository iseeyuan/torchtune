# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from .alpaca import AlpacaDataset
from .slimorca import SlimOrcaDataset

__all__ = [
    "AlpacaDataset",
    "SlimOrcaDataset",
]


def list_datasets():
    """List of available datasets supported by `get_dataset`"""
    return __all__
