# 4_inference
Project used to generate `corpus_test` using SEMPL-IT models inference.

## Getting started
### Pre-requisites
This project uses the `vllm` library. The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

Moreover, a modern GPU with more then 12GB of VRAM is required to run the model inference, for example:
* `NVIDIA RTX 4090` (24GB VRAM)

The inference operation can be performed on a local `linux` machine or on a cloud provider (e.g., AWS, vast.ai).

### Configuration
Enter in `4_inference` folder:
```sh
cd 4_inference
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

## Using `vast.ai`
Create a new private template based on `pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel` image.

Set the on-start script:
```sh
env >> /etc/environment
mkdir -p ${DATA_DIRECTORY:-/workspace/}

touch ~/.no_auto_tmux

apt-get update && apt-get install --no-install-recommends -y nano git build-essential screen && apt-get clean && rm -rf /var/lib/apt/lists/*

pip install --no-cache-dir pandas==2.2.3
pip install --no-cache-dir python-dotenv==1.0.1
pip install --no-cache-dir vllm==0.7.1
pip install --no-cache-dir bitsandbytes==0.45.1
```

Rent a machine with more than 12GB VRAM (e.g., `NVIDIA RTX4090`) using the previous created template.

Copy files on rented machine using `scp` command:
```
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ../corpus_test     root@[vast_ai_ip]:/corpus_test
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ../assets  root@[vast_ai_ip]:/assets
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ./utils       	  root@[vast_ai_ip]:/root/utils
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  -r ./*.py       	  root@[vast_ai_ip]:/root/
scp -i ~/.ssh/vast.ai -P [vast_ai_port]  .env              root@[vast_ai_ip]:/root/.env
```

Connect to the rented machine using `ssh` command:
```sh
ssh -i ~/.ssh/vast.ai -p [vast_ai_port] root@[vast_ai_ip]
```

## Usage
Run the following scripts to progressively simplify the `corpus_test`:
```sh
python 1_proofreading.py
python 2_lex
python 3_connectives.py
python 4_expressions.py
python 5_sentence_splitter.py
python 6_nominalizations.py
python 7_verbs.py
python 8_sentence_reorganizer.py
```

## Built with
* [vllm](https://github.com/vllm-project/vllm)