# -*- coding: utf-8 -*-
# Filename: model_args.py
# Author: LHM
# Description: ModelArguments
# Created: 2025-02-24
# Last Modified: 2025-02-24 by LHM
# Version: 1.0

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DataArguments:
    """
    
    """
    dataset_path: Optional[str] = field(
        default=None,
        metadata={
            "help": "List of dataset names to use for training. Use commas to seperate multiple datasets."
        }
    )