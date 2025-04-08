from utils.openai_simplifier import Simplifier
from utils.fs_utils import read_file, write_file, list_dir
from utils.loader import load_prompt, load_few_shot

PROMPT = load_prompt('7_verbs')
FEW_SHOTS = load_few_shot('7_verbs')


if __name__ == "__main__":
    simplifier = Simplifier(model=Simplifier.GPT_4O)
    for dir_to_simplify in list_dir('testing'):
        file_path = f'testing/{dir_to_simplify}/6_nominalizations.md'
        text_to_simplify = read_file(file_path)

        simplified = simplifier.simplify(PROMPT, FEW_SHOTS, text_to_simplify)
        write_file(f'testing/{dir_to_simplify}/7_verbs.md', simplified)
        print(f'Simplified {file_path}')
