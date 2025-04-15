import pandas as pd

from utils import loader
from utils import vllm_simplifier

PROMPT = loader.load_prompt('3_connectives')

if __name__ == "__main__":
    simplifier = vllm_simplifier.ConnectivesSimplifier(model="VerbACxSS/sempl-it-connectives-bnb", 
                                                       connectives=loader.load_connectives())

    test_df = pd.read_csv("../corpus_test/corpus_test_simplified.csv", encoding="utf-8")
    test_df['connectives_text'] = test_df['lex_text'].apply(lambda x: simplifier.simplify(PROMPT, x))
    test_df.to_csv("../corpus_test/corpus_test_simplified.csv", index=False)