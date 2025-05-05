# 3_model_training
Project used to train the SEMPL-IT models. It fine-tunes the `4-bit bnb` and `awq` quantized versions of `Qwen/Qwen2.5-7B-Instruct` using PEFT technique (i.e., `qlora`).

## Getting started
### Pre-requisites
This project uses the `LLaMA-Factory` library. The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

Moreover, a modern GPU with more then 30GB of VRAM is required to run the fine-tuning, for example:
* `NVIDIA L40S` (48GB VRAM)

The fine-tuning operation can be performed on a local `linux` machine or on a cloud provider (e.g., AWS, vast.ai). The fine-tuning operation requires at least one hour for each model. 

### Configuration
Enter in `3_model_training` folder:
```sh
cd 3_model_training
```

Create a `.env` file with following environment variable:
```
HF_TOKEN=...
```

### Using `python` and `pip` on local `linux` machine
Create a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

Install `flash-attn` library:
```sh
pip uninstall -y transformer-engine flash-attn ninja
pip install --no-cache-dir ninja
pip install --no-cache-dir flash-attn==2.7.2.post1 --no-build-isolation
```

## Using `vast.ai`
Create a new private template based on `pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel` image.

Set the on-start script:
```sh
env >> /etc/environment
mkdir -p ${DATA_DIRECTORY:-/workspace/}

touch ~/.no_auto_tmux

apt-get update && apt-get install --no-install-recommends -y nano git build-essential screen && apt-get clean && rm -rf /var/lib/apt/lists/*

pip install --no-cache-dir python-dotenv==1.0.1
pip install --no-cache-dir llamafactory@git+https://github.com/hiyouga/LLaMA-Factory
pip install --no-cache-dir liger-kernel==0.5.4
pip install --no-cache-dir bitsandbytes==0.45.1
pip install --no-cache-dir autoawq==0.2.8
pip install --no-cache-dir tensorboard==2.19.0
pip install --no-cache-dir nltk==3.9.1
pip install --no-cache-dir jieba==0.42.1
pip install --no-cache-dir rouge-chinese==1.0.3

pip uninstall -y transformer-engine flash-attn ninja
pip install --no-cache-dir ninja
pip install --no-cache-dir flash-attn==2.7.2.post1 --no-build-isolation
```

Rent a machine with more than 30GB VRAM (e.g., `NVIDIA L40S`) using the previous created template.

Copy files on rented machine using `scp` command:
```sh
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ./configs      root@[vast_ai_ip]:/root/configs_awq
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ./configs      root@[vast_ai_ip]:/root/configs_bnb
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ./data         root@[vast_ai_ip]:/root/data
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  ./upload_to_hf.py root@[vast_ai_ip]:/root/upload_to_hf.py
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  .env              root@[vast_ai_ip]:/root/.env
```

Connect to the rented machine using `ssh` command:
```sh
ssh -i ~/.ssh/vast.ai -p [vast_ai_port] root@[vast_ai_ip]
```

## Usage
Run the following script to generate all the `*_train.json` and `*_val.json` datasets:
```sh
python generate_ft_datasets.py
```

Run the following scripts to generate all the `config_*.yml` files:
```sh
python generate_ft_configs_awq.py
python generate_ft_configs_bnb.py
```

Run the following `llamafactory-cli` commands to start the SEMPL-IT fine-tunings:
```sh
llamafactory-cli train ./configs_awq/config_proofreading.yaml
llamafactory-cli train ./configs_awq/config_lex.yaml
llamafactory-cli train ./configs_awq/config_connectives.yaml
llamafactory-cli train ./configs_awq/config_expressions.yaml
llamafactory-cli train ./configs_awq/config_sentence-splitter.yaml
llamafactory-cli train ./configs_awq/config_nominalizations.yaml
llamafactory-cli train ./configs_awq/config_verbs.yaml
llamafactory-cli train ./configs_awq/config_sentence-reorganizer.yaml

llamafactory-cli train ./configs_bnb/config_proofreading.yaml
llamafactory-cli train ./configs_bnb/config_lex.yaml
llamafactory-cli train ./configs_bnb/config_connectives.yaml
llamafactory-cli train ./configs_bnb/config_expressions.yaml
llamafactory-cli train ./configs_bnb/config_sentence-splitter.yaml
llamafactory-cli train ./configs_bnb/config_nominalizations.yaml
llamafactory-cli train ./configs_bnb/config_verbs.yaml
llamafactory-cli train ./configs_bnb/config_sentence-reorganizer.yaml
```

Run the following scripts to upload the fine-tuned model to Hugging Face:
```sh
python upload_to_hf.py ./configs_awq/config_proofreading.yaml
python upload_to_hf.py ./configs_awq/config_lex.yaml
python upload_to_hf.py ./configs_awq/config_connectives.yaml
python upload_to_hf.py ./configs_awq/config_expressions.yaml
python upload_to_hf.py ./configs_awq/config_sentence-splitter.yaml
python upload_to_hf.py ./configs_awq/config_nominalizations.yaml
python upload_to_hf.py ./configs_awq/config_verbs.yaml
python upload_to_hf.py ./configs_awq/config_sentence-reorganizer.yaml

python upload_to_hf.py ./configs_bnb/config_proofreading.yaml
python upload_to_hf.py ./configs_bnb/config_lex.yaml
python upload_to_hf.py ./configs_bnb/config_connectives.yaml
python upload_to_hf.py ./configs_bnb/config_expressions.yaml
python upload_to_hf.py ./configs_bnb/config_sentence-splitter.yaml
python upload_to_hf.py ./configs_bnb/config_nominalizations.yaml
python upload_to_hf.py ./configs_bnb/config_verbs.yaml
python upload_to_hf.py ./configs_bnb/config_sentence-reorganizer.yaml
```

## Built with
* [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
* [Hugging Face](https://huggingface.co)
* [Qwen2.5](https://github.com/QwenLM/Qwen2.5)