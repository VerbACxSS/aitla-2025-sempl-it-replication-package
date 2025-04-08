import tiktoken
import pandas as pd

from utils import loader

TOKENIZER = tiktoken.encoding_for_model("gpt-4o")

OPENAI_BATCH_API_INPUT_COST = 1.25 / 1000 / 1000
OPENAI_BATCH_API_OUTPUT_COST = 5.00 / 1000 / 1000


def count_tokens(text):
    return len(TOKENIZER.encode(text))


def print_estimation(prompt, shots, docs):
    prompt_tokens = count_tokens(prompt)
    shots_tokens = [count_tokens(shot[0]) + count_tokens(shot[1]) for shot in shots]
    docs_tokens = [count_tokens(doc) for doc in docs]
    
    total_input_tokens = 0
    total_output_tokens = 0
    for doc_tokens in docs_tokens:
        total_input_tokens += prompt_tokens
        total_input_tokens += sum(shots_tokens)
        total_input_tokens += doc_tokens

        total_output_tokens += doc_tokens * 1.10 # 10% more tokens for output

    total_input_cost = total_input_tokens * OPENAI_BATCH_API_INPUT_COST * 1.22
    total_output_cost = total_output_tokens * OPENAI_BATCH_API_OUTPUT_COST * 1.22

    print(total_input_tokens)

    print("Input cost:", total_input_cost, "$")
    print("Output cost:", total_output_cost, "$")
