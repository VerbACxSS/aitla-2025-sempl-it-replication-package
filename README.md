# SEMPL-IT: il primo LLM per la semplificazione dell'italiano amministrativo
Giuliana Fiorentino, Vittorio Ganfi, Marco Russodivito


## Abstract
Molti studi in Italia e all'estero hanno messo in luce da decenni che il linguaggio amministrativo presenta caratteristiche strutturali e lessicali tali da ostacolare la piena fruizione dei testi scritti in questa varietà linguistica (ricordiamo solo il recente Piemontese, 2023 e il fondamentale Cortelazzo - Pellegrino, 2003 e la revisione critica dei parametri di complessità nell'italiano amministrativo contenuta in Fiorentino - Ganfi 2024). I testi istituzionali si rivelano, pertanto, poco accessibili ai cittadini che non dispongono, nel proprio repertorio, delle forme proprie del linguaggio burocratico o che più semplicemente non dispongono della competenza linguistica necessaria per la decodica di testi altamente complessi quali quelli amministrativi.

Dopo la comparsa e la diffusione dei sistemi di intelligenza artificiale modellati attraverso ampie messi di dati (d'ora innanzi: LLM *Large Language Model*) per emulare la conversazione umana (ad esempio ChatGPT), un numero crescente di studi è stato dedicato alla validazione della capacità di questi sistemi di manipolare input linguistici, accrescendo la leggibilità dei testi (tra i quali, Feng et al., 2023; Guo et al., 2023; North et al., 2023). Anche per l'italiano alcuni contributi hanno messo in mostra aspetti positivi e problemi correlati all'uso dei LLM (Tavosanis 2018; 2019).

In questo contributo viene presentato il software SEMPL-IT, un sistema di LLM progettato per semplificare il linguaggio amministrativo italiano. Il software è il frutto di una collaborazione tra studiosi di linguistica e informatica, e impiega tecniche avanzate di elaborazione del linguaggio naturale per accrescere la leggibilità dei testi inseriti come input.

Nel contributo saranno presentate le fasi che hanno condotto alla creazione di SEMPL-IT:
1. creazione del corpus ItaIst: È stato raccolto un corpus di italiano amministrativo (chiamato ItaIst), che raccoglie 208 documenti istituzionali, riconducibili ai temi della sanità, dei rifiuti e dei servizi pubblici ed emanati da enti regionali e locali di 8 regioni italiane. Il corpus consta di 840.000 token.
2. creazione di un corpus parallelo ItaIst-Sempl: È stato realizzato un corpus parallelo di ItaIst, creando una versione semplificata della banca dati di documenti amministrativi raccolti in precedenza. Per semplificare i dati linguistici è stato impiegato il modello GPT-3.5 di OpenAI. Il corpus semplificato consta di 720.000 token. Sono stati ricavati alcuni indici di leggibilità (ad esempio, l'indice di Gulpease e di Flesch-Vacca; cfr. Lusciano - Piemontese 1988; Franchina - Vacca 1986) e la percentuale del vocabolario di base (De Mauro, 2007) dei due corpora per validare l'effettiva semplificazione.
3. addestramento del Modello: I due corpora paralleli ItaIst e ItaIst-Sempl sono stati impiegati per specializzare vari LLM già preaddestrati per la generazione di testo in italiano (mT5, umT5, GPT-2 ITA, Minerva; cfr. Xue et al., 2021; de Vries - Nissim 2021; Chung et al., 2023). Scegliendo questa strategia, si è affinata la capacità del LLM di trasformare stringhe di testo riconducibili al linguaggio amministrativo in output linguistici più semplici. Il software SEMPL-IT, quindi, è stato costruito confrontando diversi LLM per trasformare testi complessi in testi più semplici, accrescendo la leggibilità dei documenti della pubblica amministrazione. Le azioni di semplificazioni riguardano gli aspetti testuali, morfosintattici e lessicali.
4. validazione: L'efficacia delle operazioni di semplificazione, effettuate da SEMPL-IT, è stata validata utilizzando strumenti automatici e giudizi di qualità di utenti esperti e comuni. Per la validazione automatica sono state confrontate varie metriche (ad esempio, gli indici di Gulpease o di Flesch-Vacca per il grado di complessità o l'indice di similarità semantica per il grado di comparabilità del contenuto). Per la validazione umana sono stati somministrati dei test a un campione bilanciato di utenti sia esperti (giuristi e funzionari pubblici) sia comuni (studenti e stranieri). Questa validazione intende saggiare la capacità dei LLM di eguagliare gli umani nei compiti di semplificazione del linguaggio amministrativo.
5. creazione di una interfaccia: È stata creata una interfaccia grafica intuitiva che permette a tutti gli utenti di inserire porzioni testuali per ottenere versioni semplificate degli input linguistici inseriti. L'interfaccia consente all'utente di ricavare automaticamente i dati relativi agli indici di complessità e di similarità semantica nelle due versioni del testo amministrativo processato da SEMPL-IT.

In conclusione, il contributo mostrerà i risultati della validazione dei LLM per la semplificazione del linguaggio amministrativo (fase IV) e illustrerà una demo di SEMPL-IT (fase V).


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