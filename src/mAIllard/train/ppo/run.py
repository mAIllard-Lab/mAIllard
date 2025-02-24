from ...model import load_tokenizer,load_model
from utils import create_ref_model, create_reward_model
from ...data import get_dataset
from .trainer import mAIllardPPOTrainer
from ...utils import plot_loss

def run_ppo(model_args, data_args, training_args,finetuning_args, generating_args,callbacks=None):
    tokenizer = load_tokenizer(model_args)
    model = load_model(model_args)

    ref_model = create_ref_model(model_args)
    reward_model = create_reward_model(model_args)

    data_collator = get_dataset(data_args, training_args, tokenizer, stage = 'ppo')

    ppo_trainer = mAIllardPPOTrainer(
        model_args=model_args,
        trainer_args=training_args,
        model=model,
        reward_model=reward_model,
        ref_model=ref_model,
        tokenizer=tokenizer,
        data_collator = data_collator
    )

    if training_args.do_train:
        ppo_trainer.ppo_train(resume_from_checkpoint = training_args.resume_from_checkpoint)
        ppo_trainer.save_model()
        ppo_trainer.save_state()
        if ppo_trainer.is_world_process_zero() and finetuning_args.plot_loss:
            plot_loss(training_args.output_dir, keys=["loss", "reward"])
        