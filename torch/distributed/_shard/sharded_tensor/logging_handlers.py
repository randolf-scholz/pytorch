#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
__all__: list[str] = []

import logging
from typing import Dict


_log_handlers: Dict[str, logging.Handler] = {
    "default": logging.NullHandler(),
}
