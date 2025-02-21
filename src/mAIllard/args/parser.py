# -*- coding: utf-8 -*-
# Filename: model_args.py
# Author: LHM
# Description: ModelArguments
# Created: 2025-02-21
# Last Modified: 2025-02-21 by LHM
# Version: 1.0

import os
import sys
import json
import yaml
from dataclasses import replace
from transformers import HfArgumentParser
from mAIllard.args.model_args import ModelArguments

def parse_args():
    """Parse Arguments

    Args:

    Returns:

    Example:
    
    """
    parser = HfArgumentParser((ModelArguments))
    if sys.argv[1].endswith('.yaml'):
        model_args = parser.parse_yaml_file(yaml_file=os.path.abspath(sys.argv[1]))[0]
        print(model_args)
        if len(sys.argv) > 2:
            model_args = replace(model_args, **{k: v for k, v in parser.parse_args_into_dataclasses(sys.argv[2:])[0].__dict__.items() if v is not None})
    elif sys.argv[1].endswith('.json'):
        model_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
        if len(sys.argv) > 2:
            model_args = replace(model_args, **{k: v for k, v in parser.parse_args_into_dataclasses(sys.argv[2:])[0].__dict__.items() if v is not None})
    else:
        model_args = parser.parse_args_into_dataclasses()
    return model_args