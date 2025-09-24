# SEMPL-IT: il primo LLM per la semplificazione dell'italiano amministrativo
Giuliana Fiorentino, Vittorio Ganfi, Marco Russodivito


## Abstract
Studi italiani e internazionali mostrano da tempo come il linguaggio amministrativo, per le sue caratteristiche strutturali e lessicali, ostacoli la piena accessibilità dei testi istituzionali ai cittadini. La diffusione dei sistemi di intelligenza artificiale basati su Large Language Model (LLM), in grado di interagire in forma conversazionale e di manipolare input linguistici, ha aperto nuove prospettive per la semplificazione dei testi. In questo contributo presentiamo SEMPL-IT, un LLM sviluppato per il linguaggio amministrativo italiano grazie alla collaborazione tra linguisti e informatici. Il modello, messo a punto attraverso pipeline sperimentale e *fine-tuning*, mira ad accrescere la leggibilità e la fruibilità dei testi. Nelle conclusioni l'esperienza viene collocata nel più ampio dibattito sulla validazione degli LLM applicati alla semplificazione amministrativa.


## Replication Package Content
The following folders contain the projects used during each phase of this work:
- `1_prompt_experiments`: folder that contains the project used to design and test all the prompts employed for simplification.
- `2_dataset_generation`: folder that contains the project used to generate `corpus_val` and `corpus_train`.
- `3_model_training`: folder that contains the project used to train and publish all the SEMPL-IT models.
- `4_inference`: folder that contains the project used to and generate the `corpus_test`.
- `5_validation`: folder that contains the project used to automatically analyze `corpus_val`, `corpus_train` and `corpus_test`.

Morover, the following folders contains:
- `assets`: folder that contains all `prompts` and `hard_connectives.txt` used to support the simplifications.
- `corpus_viewer`: folder that contains the project used to visualize in a streamlit web application the `corpus_dev`, `corpus_val` and `corpus_test`.

Lastly, the following folders contain the corpora used and generated during this work:
- `corpus_dev`: collection of 13 institutional documents manually simplified by linguists.
- `corpus_train` and `corpus_val`: collection of 1020 and 57 documents simplified by `GPT-4o` model.
- `corpus_test`: collection of 57 documents simplified by `SEMPL-IT` models.


## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.