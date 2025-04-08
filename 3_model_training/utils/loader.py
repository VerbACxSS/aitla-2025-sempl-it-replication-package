from typing import List, Tuple

from . import fs_utils


def load_prompt(step_name: str) -> str:
    return fs_utils.read_file(f'../assets/prompts/{step_name}.md')


def load_few_shot(step_name: str) -> List[Tuple[str, str]]:
    FEW_SHOT_INFO = fs_utils.read_json('../corpus_dev/few_shot_info.json')
    
    few_shots = []
    for folder in FEW_SHOT_INFO[step_name]['shots']:
        _input = fs_utils.read_file(f'../corpus_dev/{folder}/{FEW_SHOT_INFO[step_name]["prev_step"]}.md')
        _output = fs_utils.read_file(f'../corpus_dev/{folder}/{step_name}.md')
        few_shots.append((_input, _output))
    return few_shots


def load_connectives() -> List[str]:
    hard_connectives = [c.lower() for c in fs_utils.read_file('../assets/hard_connectives.txt').split('\n')]
    hard_connectives = [c + "\\b" for c in hard_connectives if (not c.endswith("*")) or (not c.endswith("]"))] 
    hard_connectives = [c.replace("a\\w*", "(a|al|allo|alla|ai|agli|alle|all')\\b") for c in hard_connectives]
    hard_connectives = [c.replace("d\\w*", "(di|del|dello|dell'|della|dei|degli|delle|dal|dallo|dall'|dalla|dai|dagli|dalle')\\b") for c in hard_connectives]
    return hard_connectives