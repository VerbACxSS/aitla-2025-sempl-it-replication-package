import pandas as pd

from utils import loader
from utils import vllm_simplifier

PROMPT = loader.load_prompt('1_proofreading')

if __name__ == "__main__":
    simplifier = vllm_simplifier.Simplifier(model="VerbACxSS/sempl-it-proofreading")

    test_df = pd.read_csv("../corpus_test/corpus_test.csv", encoding="utf-8")
    test_df['proofreading_text'] = test_df['text'].apply(lambda x: simplifier.simplify(PROMPT, x))
    test_df.to_csv("../corpus_test/corpus_test_simplified.csv", index=False)