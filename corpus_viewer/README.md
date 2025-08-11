# corpus viewer
Streamlit web application used to visualize the `corpus_dev`, `corpus_val` and `corpus_test`.

## Getting started
### Pre-requisites
This web application is developed using Streamlit framework. The following software are required to run the application:
* Python (tested with version 3.12.8)
* Pip (tested with version 23.2.1)

Alternatively, you can use a containerized version by installing:
* Docker (tested on version 28.0.1)

### Configuration
Enter in `corpus_viewer` folder:
```sh
cd corpus_viewer
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

Run the web application using `streamlit`:
```sh
streamlit run streamlit_ui.py
```

### Using `docker`
Run the web application using `docker compose`:
```sh
docker compose up --build -d
```

## Usage
The web application will be running at `http://localhost:8501` by default. 

## Built with
* [Streamlit](https://streamlit.io)