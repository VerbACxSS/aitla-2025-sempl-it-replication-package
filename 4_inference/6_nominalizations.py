import pandas as pd

from utils import loader
from utils import vllm_simplifier

PROMPT = loader.load_prompt('6_nominalizations')

if __name__ == "__main__":
    simplifier = vllm_simplifier.Simplifier(model="VerbACxSS/sempl-it-nominalizations")

    test_df = pd.read_csv("../corpus_test/corpus_test_simplified.csv", encoding="utf-8")
    test_df['nominalizations_text'] = test_df['sentence_splitter_text'].apply(lambda x: simplifier.simplify(PROMPT, x))
    test_df.to_csv("../corpus_test/corpus_test_simplified.csv", index=False)