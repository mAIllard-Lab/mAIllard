from trl import PPOTrainer, PPOConfig
from transformers import Trainer

class mAIllardPPOTrainer(PPOTrainer, Trainer):
    """
    Self-defined PPO trainer
    """
    def __init__(
        self,
        model_args,
        trainer_args,
        model,
        reward_model,
        ref_model,
        tokenizer,
        data_collator,
        processor,
        train_dataset,
        eval_dataset
    ):
        ppo_config = PPOConfig(

        )

        optimizer = ""
        scheduler = ""

        PPOTrainer.__init__(
            self,
            PPOConfig=ppo_config,
            model=model,
            ref_model=ref_model,
            reward_model=reward_model,
            train_dataset=train_dataset,
        )

