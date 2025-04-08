import os
import re

import pandas as pd


def find_hard_connectives(message):
    with open('../assets/hard_connectives.txt', 'r', encoding='utf-8') as f:
        hard_connectives = [c.lower() for c in f.read().split('\n')]
        hard_connectives = [c + "\\b" for c in hard_connectives if (not c.endswith("*")) or (not c.endswith("]"))] 
        hard_connectives = [c.replace("a\\w*", "(a|al|allo|alla|ai|agli|alle|all')\\b") for c in hard_connectives]
        hard_connectives = [c.replace("d\\w*", "(di|del|dello|dell'|della|dei|degli|delle|dal|dallo|dall'|dalla|dai|dagli|dalle')\\b") for c in hard_connectives]

        connectives_found = []
        for conn in hard_connectives:
            results = [m.group() for m in re.finditer(conn, message, re.IGNORECASE)]
            connectives_found.extend(results)
        return connectives_found


def load_dev_corpus():
    corpus = {}
    for dir in range(1, 14):
        corpus[int(dir)] = [
            open(f'../corpus_dev/{dir}/original.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/1_proofreading.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/2_lex.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/3_connectives.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/4_expressions.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/5_sentence_splitter.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/6_nominalizations.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/7_verbs.md', 'r', encoding='utf-8').read(),
            open(f'../corpus_dev/{dir}/8_sentence_reorganizer.md', 'r', encoding='utf-8').read()
        ]
    return corpus


def load_val_corpus():
    corpus = {}
    for row in pd.read_csv('../corpus_val/corpus_val_simplified.csv').to_dict(orient='records'):
        corpus[row['id']] = [
            row['text'],
            row['proofreading_text'],
            row['lex_text'],
            row['connectives_text'],
            row['expressions_text'],
            row['sentence_splitter_text'],
            row['nominalizations_text'],
            row['verbs_text'],
            row['sentence_reorganizer_text']
        ]
    return corpus

def load_test_corpus():
    corpus = {}
    for row in pd.read_csv('../corpus_test/corpus_test_simplified.csv').to_dict(orient='records'):
        corpus[row['id']] = [
            row['text'],
            row['proofreading_text'],
            row['lex_text'],
            row['connectives_text'],
            row['expressions_text'],
            row['sentence_splitter_text'],
            row['nominalizations_text'],
            row['verbs_text'],
            row['sentence_reorganizer_text']
        ]
    return corpus