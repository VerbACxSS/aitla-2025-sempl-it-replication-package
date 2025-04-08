# 2_dataset_generation
Project used to extract `corpus_train`, `corpus_test` and `corpus_val` from `ItaIst` corpus.

## Getting started
### Pre-requisites
The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

### Configuration
Enter in `2_dataset_generation` folder:
```sh
cd 2_dataset_generation
```

### Using `python` and `pip`
Create a virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the following scripts to extract `corpus_train`, `corpus_test` and `corpus_val` from `ItaIst` corpus:
```sh
python create_datasets.py
```

Run the following scripts to generate the `.jsonl` file to be used in OpenAI Batch API. Each script will create two files — `*_train_input.json` and `*_val_input.jsonl` — and save them in `api_files` folder. These files should then be uploaded to the OpenAI Batch API. After the batch job completes, download the corresponding `*_train_output.json` and `*_val_output.jsonl` files. Once done, proceed to the next script.
```sh
python 1_proofreading.py
# upload 1_proofreading_train_input.json
# upload 1_proofreading_val_input.json
# download 1_proofreading_train_output.json
# download 1_proofreading_val_output.json

python 2_lex
# upload 2_lex_train_input.json
# upload 2_lex_val_input.json
# download 2_lex_train_output.json
# download 2_lex_val_output.json

python 3_connectives.py
# upload 3_connectives_train_input.json
# upload 3_connectives_val_input.json
# download 3_connectives_train_output.json
# download 3_connectives_val_output.json

python 4_expressions.py
# upload 4_expressions_train_input.json
# upload 4_expressions_val_input.json
# download 4_expressions_train_output.json
# download 4_expressions_val_output.json

python 5_sentence_splitter.py
# upload 5_sentence_splitter_train_input.json
# upload 5_sentence_splitter_val_input.json
# download 5_sentence_splitter_train_output.json
# download 5_sentence_splitter_val_output.json

python 6_nominalizations.py
# upload 6_nominalizations_train_input.json
# upload 6_nominalizations_val_input.json
# download 6_nominalizations_train_output.json
# download 6_nominalizations_val_output.json

python 7_verbs.py
# upload 7_verbs_train_input.json
# upload 7_verbs_val_input.json
# download 7_verbs_train_output.json
# download 7_verbs_val_output.json

python 8_sentence_reorganizer.py
# upload 8_sentence_reorganizer_train_input.json
# upload 8_sentence_reorganizer_val_input.json
# download 8_sentence_reorganizer_train_output.json
# download 8_sentence_reorganizer_val_output.json
```

Run the following script to generate the simplified of `corpus_train` and `corpus_val` from `*_train_output.jsonl` and `*_val_output.jsonl` files.
```sh
python assembly_simplified_dataset.py
```
