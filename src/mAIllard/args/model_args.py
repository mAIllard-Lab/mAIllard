# -*- coding: utf-8 -*-
# Filename: model_args.py
# Author: LHM
# Description: ModelArguments
# Created: 2025-02-21
# Last Modified: 2025-02-21 by LHM
# Version: 1.0

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ModelArguments:
    """
    
    """
    model_name_or_path: Optional[str] = field(
        default=None,
        metadata={
            "help": "Path to the model weights (local / hf_url / ms_url)."
        }
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={
            "help": "Cache directory of huggingface."
        }
    )
    use_fast_tokenizer: bool = field(
        default=True,
        metadata={
            "help": "Whether or not to use fast tokenizer."
        }
    )
    