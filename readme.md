# How to generate Lunar data

## Install Python 3.12

```shell
pyenv install 3.12
```

## Create virtual environment

```shell
pyenv local 3.12
python -m venv venv
source venv/bin/activate
```

## Install dependencies

```shell
pip install -r requirements.txt
```

## Generate Lunar data

```shell
python generate_lunar_data.py
```
