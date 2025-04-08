# 5_validation
Project used to validate SEMPL-IT models.

## Getting started
### Pre-requisites
The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

### Configuration
Enter in `5_validation` folder:
```sh
cd 5_validation
```

### Using `python` and `pip`
Create a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
Run the following script to extract metrics from `corpus_train`, `corpus_val` and `corpus_test`:
```sh
python metrics_extractor.py
```

Run the following notebooks to visualize the metrics of `corpus_train`, `corpus_val` and `corpus_test`
```sh
corpus_train_metrics.ipynb
corpus_val_metrics.ipynb
corpus_test_metrics.ipynb
```

Run the following notebook to visualize the manual validation of the `corpus_test`:
```sh
corpus_test_manual_validation.ipynb
```