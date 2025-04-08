import pandas as pd

from utils.openai_batch_simplifier import BatchSimplifier
from utils.fs_utils import read_jsonl, write_jsonl
from utils.loader import load_prompt, load_few_shot
from utils.openai_cost_estimator import print_estimation

PROMPT = load_prompt('1_proofreading')
FEW_SHOTS = load_few_shot('1_proofreading')


if __name__ == "__main__":
    simplifier = BatchSimplifier(model=BatchSimplifier.GPT_4O)

    print("Train...")
    train_ids = [id for id in pd.read_csv('../corpus_train/corpus_train.csv')['id'].to_list()]
    train_docs = [text for text in pd.read_csv('../corpus_train/corpus_train.csv')['text'].to_list()]

    train_output = []
    for id, text_to_simplify in zip(train_ids, train_docs):
        train_output.append(simplifier.generate_request(id, PROMPT, FEW_SHOTS, text_to_simplify))
    write_jsonl('api_files/1_proofreading_train_input.jsonl', train_output)
    print_estimation(PROMPT, FEW_SHOTS, train_docs)

    print("Val...")
    val_ids = [id for id in pd.read_csv('../corpus_val/corpus_val.csv')['id'].to_list()]
    val_docs = [text for text in pd.read_csv('../corpus_val/corpus_val.csv')['text'].to_list()]

    val_output = []
    for id, text_to_simplify in zip(val_ids, val_docs):
        val_output.append(simplifier.generate_request(id, PROMPT, FEW_SHOTS, text_to_simplify))
    write_jsonl('api_files/1_proofreading_val_input.jsonl', val_output)

    print_estimation(PROMPT, FEW_SHOTS, val_docs)
