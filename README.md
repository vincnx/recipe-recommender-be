# Recipe Recommender

**i run this project run normally on python 3.12.11, when i try to run this on 3.13.5 this will generate error because of gensim library**

## Instalation

1. clone this repository to your local machine

```bash
git clone https://github.com/vincnx/recipe-recommender-be.git
```

2. generate & activate python virtual environment

```bash
# i use 3.12 here because when i try on 3.13 it will break and gensim library cannot installed
python3.12 -m venv .venv
```

- activate venv (windows)

```bash
.venv\Scripts\activate
```

- activate venv (linux/mac)

```bash
source .venv/bin/activate
```

3. install the project dependencies

```bash
pip install -r requirements.txt
```

4. add config.yml file for each domain see the example from config.example.yml

5. download the model from [here](https://drive.google.com/drive/folders/1MlSzpQikctFdDEKltyddilCRDWttkROp?usp=sharing), place it in models directory

## Usage

### Use the chatbot

1. run the project

```bash
python app.py
```

### Optional

- configure port or host in app.py (default host: 0.0.0.0, port: 8080)
