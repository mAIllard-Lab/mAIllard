from ..args.parser import parse_args
from pt import run_pt
from sft import run_sft
from rsft import run_rsft
from ppo import run_ppo
from grpo import run_grpo

def log_metrics():
    pass

def run_trainer(args, callbacks=None):
    args = parse_args(args)
    model_args, data_args, training_args, finetuning_args, generating_args = args
    
    if finetuning_args.stage == 'pt':
        run_pt(model_args, data_args, training_args,finetuning_args,callbacks)
    elif finetuning_args.stage == 'sft':
        run_sft(model_args, data_args, training_args,finetuning_args, generating_args,callbacks)
    elif finetuning_args.stage == 'rsft':
        run_rsft(model_args, data_args, training_args,finetuning_args, generating_args,callbacks)
    elif finetuning_args.stage == 'ppo':
        run_ppo(model_args, data_args, training_args,finetuning_args, generating_args,callbacks)
    elif finetuning_args.stage == 'grpo':  
        run_grpo(model_args, data_args, training_args,finetuning_args, generating_args,callbacks)
    else:
        raise NotImplementedError(f"Unsupport stage: {finetuning_args.stage}")