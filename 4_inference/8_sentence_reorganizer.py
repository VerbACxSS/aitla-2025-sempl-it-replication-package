import pandas as pd

from utils import loader
from utils import vllm_simplifier

PROMPT = loader.load_prompt('8_sentence_reorganizer')

if __name__ == "__main__":
    simplifier = vllm_simplifier.Simplifier(model="VerbACxSS/sempl-it-sentence-reorganizer-bnb")

    test_df = pd.read_csv("../corpus_test/corpus_test_simplified.csv", encoding="utf-8")
    test_df['sentence_reorganizer'] = test_df['verbs_text'].apply(lambda x: simplifier.simplify(PROMPT, x))
    test_df.to_csv("../corpus_test/corpus_test_simplified.csv", index=False)