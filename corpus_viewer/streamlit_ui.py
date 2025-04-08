import re

import streamlit as st
from st_diff_viewer import diff_viewer

import utils

corpora = {
    'corpus_dev': utils.load_dev_corpus(),
    'corpus_val': utils.load_val_corpus(),
    'corpus_test': utils.load_test_corpus()
}
corpora['corpus_dev'] = dict(sorted(corpora['corpus_dev'].items()))
corpora['corpus_val'] = dict(sorted(corpora['corpus_val'].items()))
corpora['corpus_test'] = dict(sorted(corpora['corpus_test'].items()))


def draw_diff(old_text, new_text, component_instance):
    diff_viewer(old_text=old_text,
                new_text=new_text,
                split_view=True,
                hide_line_numbers=True,
                disabled_word_diff=False,
                extra_lines_surrounding_diff=True,
                component_instance=component_instance,
                styles=DIFF_STYLE)

# Setup page
st.set_page_config(layout="wide")
DIFF_STYLE = {"contentText": {"white-space": 'normal'}, "wordDiff": {"display": "inline", "padding": "0px", "word-break": "unset"}}

# Title
st.title("Dataset validation")

# Side bar
st.sidebar.header("Filtri")
dataset_choice = st.sidebar.radio("Seleziona il dataset:", options=["corpus_dev", "corpus_val", "corpus_test"])
document_choice = st.sidebar.selectbox("Seleziona il documento:", options=corpora[dataset_choice].keys())

# Filter document
document = corpora[dataset_choice][document_choice]

# Draw diffs
draw_diff(old_text=document[0],
          new_text=document[8],
          component_instance='a')

with st.expander('1_proofreading'):
    draw_diff(old_text=document[0],
              new_text=document[1],
              component_instance='1')

with st.expander('2_lex'):
    draw_diff(old_text=document[1],
              new_text=document[2],
              component_instance='2')

with st.expander('3_connectives'):
    draw_diff(old_text=document[2],
              new_text=document[3],
              component_instance='3')
    st.write(f"Connectives found: {utils.find_hard_connectives(document[2])}")

with st.expander('4_expressions'):
    draw_diff(old_text=document[3],
              new_text=document[4],
              component_instance='4')

with st.expander('5_sentence_splitter'):
    draw_diff(old_text=document[4],
              new_text=document[5],
              component_instance='5')

with st.expander('6_nominalizations'):
    draw_diff(old_text=document[5],
              new_text=document[6],
              component_instance='6')

with st.expander('7_verbs'):
    draw_diff(old_text=document[6],
              new_text=document[7],
              component_instance='7')

with st.expander('8_sentence_reorganizer'):
    draw_diff(old_text=document[7],
            new_text=document[8],
            component_instance='8')