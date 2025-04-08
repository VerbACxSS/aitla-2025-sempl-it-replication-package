import json

import pandas as pd
from tqdm import tqdm

from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer


def extract_metrics(text, result, similarity_results=None, diff_results=None):
    metrics = {
        'n_tokens': result.basic.n_tokens,
        'n_tokens_all': result.basic.n_tokens_all,
        'n_chars': result.basic.n_chars,
        'n_chars_all': result.basic.n_chars_all,
        'n_syllables': result.basic.n_syllables,
        'n_words': result.basic.n_words,
        'n_unique_lemmas': result.basic.n_unique_lemmas,
        'n_sentences': result.basic.n_sentences,
        # Pos
        'n_other': result.pos.n_other,
        'n_nouns': result.pos.n_nouns,
        'n_verbs': result.pos.n_verbs,
        'n_number': result.pos.n_number,
        'n_symbols': result.pos.n_symbols,
        'n_adverbs': result.pos.n_adverbs,
        'n_articles': result.pos.n_articles,
        'n_pronouns': result.pos.n_pronouns,
        'n_particles': result.pos.n_particles,
        'n_adjectives': result.pos.n_adjectives,
        'n_prepositions': result.pos.n_prepositions,
        'n_proper_nouns': result.pos.n_proper_nouns,
        'n_punctuations': result.pos.n_punctuations,
        'n_interjections': result.pos.n_interjections,
        'n_coordinating_conjunctions': result.pos.n_coordinating_conjunctions,
        'n_subordinating_conjunctions': result.pos.n_subordinating_conjunctions,
        # Verbs
        'n_active_verbs': result.verbs.n_active_verbs,
        'n_passive_verbs': result.verbs.n_passive_verbs,
        # Expressions
        'n_latinisms': result.expression.n_latinisms,
        'n_difficult_connectives': result.expression.n_difficult_connectives,
        # Readability
        'ttr': result.readability.ttr,
        'gulpease': result.readability.gulpease,
        'flesch_vacca': result.readability.flesch_vacca,
        'lexical_density': result.readability.lexical_density,
        # VdB
        'n_vdb': result.vdb.n_vdb_tokens,
        'n_vdb_fo': result.vdb.n_vdb_fo_tokens,
        'n_vdb_au': result.vdb.n_vdb_au_tokens,
        'n_vdb_ad': result.vdb.n_vdb_ad_tokens,
    }
    raw_data = {
        'tokens': result.basic.tokens,
        'lemmas': result.basic.lemmas,
        'difficult_connectives': result.expression.difficult_connectives,
        'latinisms': result.expression.latinisms,
    }
    if similarity_results is not None and diff_results is not None:
        metrics.update({
            'semantic_similarity': similarity_results.semantic_similarity,
            'editdistance': diff_results.editdistance,
            'n_added_tokens': diff_results.n_added_tokens,
            'n_deleted_tokens': diff_results.n_deleted_tokens,
            'n_added_vdb_tokens': diff_results.n_added_vdb_tokens,
            'n_deleted_vdb_tokens': diff_results.n_deleted_vdb_tokens,
        })
    return metrics, raw_data


if __name__ == "__main__":
    # DATASETS = ["corpus_val", "corpus_train", "corpus_test"]
    # TEXTS = ['text', 'proofreading_text', 'lex_text', 'connectives_text', 'expressions_text', 'sentence_splitter_text', 'nominalizations_text', 'verbs_text', 'sentence_reorganizer_text']

    DATASETS = ["corpus_test"]
    TEXTS = ['text', 'sentence_reorganizer_text']	

    for DATASET in DATASETS:
        # Load the dataset
        corpus_df = pd.read_csv(f"../{DATASET}/{DATASET}_simplified.csv", encoding="utf-8")
        corpus_df = corpus_df[TEXTS]

        # Extract metrics
        metrics = {TEXT:[] for TEXT in TEXTS}
        raw_data = {TEXT:[] for TEXT in TEXTS}
        for TEXT in TEXTS:
            print(f"Processing {TEXT}...")
            for row in tqdm(corpus_df.to_dict(orient="records")):
                if TEXT == 'text':
                    result = TextAnalyzer(row[TEXT])
                    metrics[TEXT].append(extract_metrics(row[TEXT], result)[0])
                    raw_data[TEXT].append(extract_metrics(row[TEXT], result)[1])
                else:
                    result = SimplificationAnalyzer(row[TEXTS[0]], row[TEXT])
                    metrics[TEXT].append(extract_metrics(row[TEXT], result.simplified, result.similarity, result.diff)[0])
                    raw_data[TEXT].append(extract_metrics(row[TEXT], result.simplified)[1])

        # Save metrics
        metrics_dfs = {TEXT: pd.DataFrame(metrics[TEXT]) for TEXT in TEXTS}
        for TEXT in TEXTS:
            metrics_dfs[TEXT].to_csv(f"./metrics/{DATASET}/{TEXT}_metrics.csv", index=False)
            json.dump(raw_data[TEXT], open(f"./metrics/{DATASET}/{TEXT}_raw_data.json", "w", encoding="utf-8"), ensure_ascii=False)