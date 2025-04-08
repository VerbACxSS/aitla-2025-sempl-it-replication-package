from utils.openai_simplifier import Simplifier, ConnectivesSimplifier
from utils.fs_utils import read_file, write_file, list_dir
from utils.loader import load_prompt, load_few_shot, load_connectives

PROMPT = load_prompt('3_connectives')
FEW_SHOTS = load_few_shot('3_connectives')
HARD_CONNECTIVES = load_connectives()


if __name__ == "__main__":
    simplifier = ConnectivesSimplifier(connectives=HARD_CONNECTIVES, model=Simplifier.GPT_4O)
    for dir_to_simplify in list_dir('testing'):
        file_path = f'testing/{dir_to_simplify}/2_lex.md'
        text_to_simplify = read_file(file_path)

        simplified = simplifier.simplify(PROMPT, FEW_SHOTS, text_to_simplify)
        write_file(f'testing/{dir_to_simplify}/3_connectives.md', simplified)
        print(f'Simplified {file_path}')
