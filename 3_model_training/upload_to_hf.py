import os
import sys

import yaml
from dotenv import load_dotenv

from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login, upload_folder


load_dotenv()

if __name__ == "__main__":
    if len(sys.argv) <= 0:
        print("Usage: python upload_to_hf.py <config_file>")
        sys.exit(1)
    
    print(f"Loading config from {sys.argv[1]}")
    config = yaml.safe_load(open(sys.argv[1], "r"))
    model_name = config['model_name_or_path']
    model_folder = config['output_dir']
    hub_model_id = config['hub_model_id']

    print("Logging in to Hugging Face")
    login(token=os.getenv("HF_TOKEN"))

    print("Loading model and tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(model_folder)
    model = AutoModelForCausalLM.from_pretrained(config['model_name_or_path'])
    model = PeftModel.from_pretrained(model, model_id=model_folder)

    print("Pushing model to Hugging Face")
    # Push model
    model.push_to_hub(
        repo_id=hub_model_id,
        revision="main"
    )
    # Push tokenizer
    tokenizer.push_to_hub(
        repo_id=hub_model_id,
        revision="main"
    )
    # Push tensorboard logs
    upload_folder(
        repo_id=hub_model_id,
        revision="main",
        folder_path=f'{model_folder}/runs',
        path_in_repo="logs"
    )

    print("Model uploaded successfully to Hugging Face")