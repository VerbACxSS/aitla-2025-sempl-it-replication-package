import pandas as pd

from utils import fs_utils
from utils.openai_batch_simplifier import BatchSimplifier


def find_in_batch_output(batch_output, id):
    batch_output = [BatchSimplifier.parse_response(x) for x in batch_output]
    return [y[1] for y in batch_output if y[0] == str(id)][0]


if __name__ == "__main__":
    # Validation
    val_proofreading_output = fs_utils.read_jsonl('api_files/1_proofreading_val_output.jsonl')
    val_lex_output = fs_utils.read_jsonl('api_files/2_lex_val_output.jsonl')
    val_connectives_output = fs_utils.read_jsonl('api_files/3_connectives_val_output.jsonl')
    val_expressions_output = fs_utils.read_jsonl('api_files/4_expressions_val_output.jsonl')
    val_sentence_splitter_output = fs_utils.read_jsonl('api_files/5_sentence_splitter_val_output.jsonl')
    val_nominalizations_output = fs_utils.read_jsonl('api_files/6_nominalizations_val_output.jsonl')
    val_verbs_output = fs_utils.read_jsonl('api_files/7_verbs_val_output.jsonl')
    val_sentence_reorganizer_output = fs_utils.read_jsonl('api_files/8_sentence_reorganizer_val_output.jsonl')

    val_df = pd.read_csv('../corpus_val/corpus_val.csv', encoding="utf-8")
    val_df['proofreading_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_proofreading_output, x))
    val_df['lex_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_lex_output, x))
    val_df['connectives_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_connectives_output, x))
    val_df['expressions_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_expressions_output, x))
    val_df['sentence_splitter_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_sentence_splitter_output, x))
    val_df['nominalizations_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_nominalizations_output, x))
    val_df['verbs_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_verbs_output, x))
    val_df['sentence_reorganizer_text'] = val_df['id'].apply(lambda x: find_in_batch_output(val_sentence_reorganizer_output, x))
    val_df.to_csv('../corpus_val/corpus_val_simplified.csv', index=False)

    # Train
    train_proofreading_output = fs_utils.read_jsonl('api_files/1_proofreading_train_output.jsonl')
    train_lex_output = fs_utils.read_jsonl('api_files/2_lex_train_output.jsonl')
    train_connectives_output = fs_utils.read_jsonl('api_files/3_connectives_train_output.jsonl')
    train_expressions_output = fs_utils.read_jsonl('api_files/4_expressions_train_output.jsonl')
    train_sentence_splitter_output = fs_utils.read_jsonl('api_files/5_sentence_splitter_train_output.jsonl')
    train_nominalizations_output = fs_utils.read_jsonl('api_files/6_nominalizations_train_output.jsonl')
    train_verbs_output = fs_utils.read_jsonl('api_files/7_verbs_train_output.jsonl')
    train_sentence_reorganizer_output = fs_utils.read_jsonl('api_files/8_sentence_reorganizer_train_output.jsonl')

    train_df = pd.read_csv('../corpus_train/corpus_train.csv', encoding="utf-8")
    train_df['proofreading_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_proofreading_output, x))
    train_df['lex_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_lex_output, x))
    train_df['connectives_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_connectives_output, x))
    train_df['expressions_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_expressions_output, x))
    train_df['sentence_splitter_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_sentence_splitter_output, x))
    train_df['nominalizations_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_nominalizations_output, x))
    train_df['verbs_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_verbs_output, x))
    train_df['sentence_reorganizer_text'] = train_df['id'].apply(lambda x: find_in_batch_output(train_sentence_reorganizer_output, x))
    train_df.to_csv('../corpus_train/corpus_train_simplified.csv', index=False)