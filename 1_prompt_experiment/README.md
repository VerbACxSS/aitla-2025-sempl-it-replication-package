# 1_prompt_experiment
Project used to test and experiment simplification using different prompts.

## Getting started
### Pre-requisites
This project uses the official `openai` library. The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

### Configuration
Enter in `1_prompt_experiment` folder:
```sh
cd 1_prompt_experiment
```

Create a `.env` file with following environment variable:
```
OPENAI_API_KEY=...
```

### Using `python` and `pip`
Create a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
Run the following scripts to progressively simplify documents in `testing` folder:
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
* [OpenAI](https://openai.com)
