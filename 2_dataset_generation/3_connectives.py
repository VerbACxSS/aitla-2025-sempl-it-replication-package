from utils.openai_batch_simplifier import BatchSimplifier, ConnectivesBatchSimplifier
from utils.fs_utils import read_jsonl, write_jsonl
from utils.loader import load_prompt, load_few_shot, load_connectives
from utils.openai_cost_estimator import print_estimation

PROMPT = load_prompt('3_connectives')
FEW_SHOTS = load_few_shot('3_connectives')
HARD_CONNECTIVES = load_connectives()


if __name__ == "__main__":
    simplifier = ConnectivesBatchSimplifier(connectives=HARD_CONNECTIVES, model=BatchSimplifier.GPT_4O)

    print("Train...")
    train_ids = [BatchSimplifier.parse_response(x)[0] for x in read_jsonl('api_files/2_lex_train_output.jsonl')]
    train_docs = [BatchSimplifier.parse_response(x)[1] for x in read_jsonl('api_files/2_lex_train_output.jsonl')]

    train_output = []
    for id, text_to_simplify in zip(train_ids, train_docs):
        train_output.append(simplifier.generate_request(id, PROMPT, FEW_SHOTS, text_to_simplify))
    write_jsonl('api_files/3_connectives_train_input.jsonl', train_output)
    print_estimation(PROMPT, FEW_SHOTS, train_docs)

    print("Val...")
    val_ids = [BatchSimplifier.parse_response(x)[0] for x in read_jsonl('api_files/2_lex_val_output.jsonl')]
    val_docs = [BatchSimplifier.parse_response(x)[1] for x in read_jsonl('api_files/2_lex_val_output.jsonl')]

    val_output = []
    for id, text_to_simplify in zip(val_ids, val_docs):
        val_output.append(simplifier.generate_request(id, PROMPT, FEW_SHOTS, text_to_simplify))
    write_jsonl('api_files/3_connectives_val_input.jsonl', val_output)
    print_estimation(PROMPT, FEW_SHOTS, val_docs)

