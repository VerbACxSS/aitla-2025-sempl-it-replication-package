import re

import numpy as np
import pandas as pd

from utils import openai_cost_estimator

DOCUMENT_IDS = [
    '396505aaf67c46b9ec1a6818d8fb9af6', # lazio - garbage - service-charter (s-ItaIst)
    'd59699a3bdb772fa0f95a52f333f5e41', # calabria - garbage - service-charter
    '060f65a05e57c2888b59db715b5e522a', # lombardia - garbage - service-charter
    'c32b7b5b8cd45ef9493650ada7da3473', # veneto - garbage - service-charter

    '6d52bcc84ee3fa9bfec74bb009537bd2', # molise - garbage - tender (s-ItaIst)
    'f25789eab1c7f3c362d1d7efec057f9c', # basilicata - garbage - tender
    '61f5d72271c1f28084d78c0c8bbf1cee', # toscana - garbage - tender
    '88cd4ab12d20cfd81d52d47bf52b2753', # campania - garbage - tender
    
    '3e0abd25f3bcf417e9e0a8b74e158ef5', # lombardia - healthcare - accreditation (s-ItaIst)
    '9f8d4ec7b121af7da261c95fddab5857', # lazio - healthcare - accreditation
    '1a7e52b02aff23418abb4795d749c8be', # calabria - healthcare - accreditation
    '305797092e4281c1efa5f3733a498f2f', # campania - healthcare - accreditation
    
    '99bdc9fdd8097f067f77cb220074b1b5', # basilicata - healthcare - planning acts (s-ItaIst)
    'fbeb264c2b6ab70678f08e1ce8d07df3', # molise - healthcare - planning acts
    '1871c1a6d881a321e83a70ab9745cc19', # toscana - healthcare - planning acts
    'cca682c8e597276a9313e6eff21fe065', # veneto - healthcare - planning acts

    '70da2ae575436d19518deae1ff2125b0', # toscana - public_services - service-charter (s-ItaIst)
    'aae5c6f0c213946d265cb98c08106c0b', # veneto - public_services - service-charter (s-ItaIst)
    '2f4c39c9fb796e5066ac28770c5724d6', # campania - public_services - service-charter (s-ItaIst)
    '9505701ca5370bb3f3e83d38bdd10369', # basilicata - public_services - service-charter
    
    '07108e7d68b7e897ed6a800be9802105', # calabria - public_services - public_holdings_rationalization (s-ItaIst)
    '3b44ba84a9530c7e853f26b8e78b3860', # lazio - public_services - public_holdings_rationalization
    'afd87cd7113e3374c8c3b1274cfb39c2', # molise - public_services - public_holdings_rationalization
    '2484a1f62c107abadc920f82340d1613', # lombardia - public_services - public_holdings_rationalization
]


def parse_heading_level(row):
    full_text = f'# {row["title"]}\n{row["content"]}'

    pattern = r'(?m)^(#+)\s*(.+)$'
    matches = list(re.finditer(pattern, full_text))

    parsed_data = []
    for i, match in enumerate(matches):
        heading_level = len(match.group(1))
        heading = match.group(2).strip()
        
        start_idx = match.end()
        if i + 1 < len(matches):
            end_idx = matches[i + 1].start()
        else:
            end_idx = len(full_text)
        content = full_text[start_idx:end_idx].strip()

        if content:
            r = row.copy()
            r['title'] = heading
            r['content'] = content
            r['tokens'] = openai_cost_estimator.count_tokens(content)
            parsed_data.append(r.copy())
    return parsed_data


if __name__ == "__main__":
    print("Downloading ItaIst corpus...")
    corpus = pd.read_csv("hf://datasets/VerbACxSS/ItaIst/corpus.csv", encoding="utf-8")
    print(corpus.shape)

    print("Selecting corpus documents...")
    corpus = corpus[corpus['document_id'].isin(DOCUMENT_IDS)]
    print(corpus.shape)

    print("Parsing corpus...")
    full_dataset = []
    for row in corpus.to_dict(orient="records"):
        parsed = parse_heading_level(row)
        full_dataset.extend(parsed)
    
    print("Filtering corpus...")
    full_dataset = [x for x in full_dataset if x['tokens'] > 60 and x['tokens'] < 2048]
    full_dataset = pd.DataFrame(full_dataset)
    full_dataset = full_dataset.drop(columns=["tokens", "progress"])

    print("Splitting corpus...")
    train_set, test_set, val_set = np.split(full_dataset.sample(frac=1), [int(.9*len(full_dataset)), int(.95*len(full_dataset))])
    print(train_set.shape)
    print(test_set.shape)
    print(val_set.shape)

    print("Sorting corpora and creating id and ...")
    train_set = train_set.sort_values(by=['document_id'])
    test_set = test_set.sort_values(by=['document_id'])
    val_set = val_set.sort_values(by=['document_id'])
    
    train_set['id'] = np.arange(0, train_set.shape[0])
    test_set['id'] = np.arange(0, test_set.shape[0])
    val_set['id'] = np.arange(0, val_set.shape[0])

    print("Saving corpora...")
    train_set.to_csv("../corpus_train/corpus_train.csv", index=False, encoding="utf-8")
    test_set.to_csv("../corpus_test/corpus_test.csv", index=False, encoding="utf-8")
    val_set.to_csv("../corpus_val/corpus_val.csv", index=False, encoding="utf-8")
