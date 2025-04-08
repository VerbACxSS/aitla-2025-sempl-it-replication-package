import os
import json
from typing import List


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_json(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_jsonl(file_path: str) -> List[dict]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]


def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def write_json(file_path: str, content: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4)


def write_jsonl(file_path: str, content: List[dict]) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('')

    with open(file_path, 'a', encoding='utf-8') as file:
        for line in content:
            file.write(json.dumps(line) + '\n')


def list_dir(dir_path: str) -> List[str]:
    return os.listdir(dir_path)
