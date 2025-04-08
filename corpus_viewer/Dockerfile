FROM python:3.12.2-slim-bookworm

WORKDIR /app

COPY corpus_viewer/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY corpus_viewer/utils.py ./
COPY corpus_viewer/streamlit_ui.py ./
COPY assets/hard_connectives.txt ../assets/hard_connectives.txt
COPY corpus_dev ../corpus_dev
COPY corpus_val ../corpus_val
COPY corpus_test ../corpus_test

ENTRYPOINT ["streamlit", "run", "streamlit_ui.py"]