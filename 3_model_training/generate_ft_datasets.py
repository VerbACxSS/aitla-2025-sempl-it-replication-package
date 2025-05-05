import re

import pandas as pd

from utils import fs_utils, loader

HARD_CONNECTIVES = loader.load_connectives()
DATASET_INFOS = {
    # proofreading
    "proofreading_train": {
        "prompt": "../assets/prompts/1_proofreading.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "text",	
        "output_col": "proofreading_text"
    },
    "proofreading_val": {
        "prompt": "../assets/prompts/1_proofreading.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "text",
        "output_col": "proofreading_text"
    },
    # lex
    "lex_train": {
        "prompt": "../assets/prompts/2_lex.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "proofreading_text",
        "output_col": "lex_text"
    },
    "lex_val": {
        "prompt": "../assets/prompts/2_lex.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "proofreading_text",
        "output_col": "lex_text"
    },
    # connectives
    "connectives_train": {
        "prompt": "../assets/prompts/3_connectives.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "lex_text",
        "output_col": "connectives_text"
    },
    "connectives_val": {
        "prompt": "../assets/prompts/3_connectives.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "lex_text",
        "output_col": "connectives_text"
    },
    # expressions
    "expressions_train": {
        "prompt": "../assets/prompts/4_expressions.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "connectives_text",
        "output_col": "expressions_text"
    },
    "expressions_val": {
        "prompt": "../assets/prompts/4_expressions.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "connectives_text",
        "output_col": "expressions_text"
    },
    # sentence_splitter
    "sentence_splitter_train": {
        "prompt": "../assets/prompts/5_sentence_splitter.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "expressions_text",
        "output_col": "sentence_splitter_text"
    },
    "sentence_splitter_val": {
        "prompt": "../assets/prompts/5_sentence_splitter.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "expressions_text",
        "output_col": "sentence_splitter_text"
    },
    # nominalizations
    "nominalizations_train": {
        "prompt": "../assets/prompts/6_nominalizations.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "sentence_splitter_text",
        "output_col": "nominalizations_text"
    },
    "nominalizations_val": {
        "prompt": "../assets/prompts/6_nominalizations.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "sentence_splitter_text",
        "output_col": "nominalizations_text"
    },
    # verbs
    "verbs_train": {
        "prompt": "../assets/prompts/7_verbs.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "nominalizations_text",
        "output_col": "verbs_text"
    },
    "verbs_val": {
        "prompt": "../assets/prompts/7_verbs.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "nominalizations_text",
        "output_col": "verbs_text"
    },
    # sentence_reorganizer
    "sentence_reorganizer_train": {
        "prompt": "../assets/prompts/8_sentence_reorganizer.md",
        "dataset": "../corpus_train/corpus_train_simplified.csv",
        "input_col": "verbs_text",
        "output_col": "sentence_reorganizer_text"
    },
    "sentence_reorganizer_val": {
        "prompt": "../assets/prompts/8_sentence_reorganizer.md",
        "dataset": "../corpus_val/corpus_val_simplified.csv",
        "input_col": "verbs_text",
        "output_col": "sentence_reorganizer_text"
    },
}


def add_connectives(message):
    connectives_found = []
    for conn in HARD_CONNECTIVES:
        results = [m.group() for m in re.finditer(conn, message, re.IGNORECASE)]
        connectives_found.extend(results)
    
    output = "## Testo\n" + message + "\n\n## Connettivi\n"
    if len(connectives_found) == 0:
        output += "[Nessuno]"
    else:
        for c in connectives_found:
            output += f"- {c}\n"
    return output


if __name__ == "__main__":
    dataset_info_out = {}
    for dataset_name, info in DATASET_INFOS.items():
        dataset_info_out[dataset_name] = {
            "file_name": f"{dataset_name}.json",
            "formatting": "sharegpt",
            "columns": {
                "messages": "messages"
            },
            "tags": {
                "role_tag": "role",
                "content_tag": "content",
                "user_tag": "user",
                "assistant_tag": "assistant",
                "system_tag": "system"
            }
        }
    fs_utils.write_json("data/dataset_info.json", dataset_info_out)

    for name, info in DATASET_INFOS.items():
        prompt = fs_utils.read_file(info["prompt"])

        pandas_df = pd.read_csv(info["dataset"])

        out = []
        for row in pandas_df.to_dict(orient="records"):
            out.append({
                "messages": [
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": row[info["input_col"]] if not name.startswith("connectives") else add_connectives(row[info["input_col"]])
                    },
                    {
                        "role": "assistant",
                        "content": row[info["output_col"]]
                    }
                ]
            })
        fs_utils.write_json(f"data/{name}.json", out)

