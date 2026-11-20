# Caesar Cipher Web Application

## Software Engineering Practice #05 Project
Simple encryption/decryption Web App

## Structure
```text
SE_5/
├── app.py - main app logic
├── cipher.py - cipher logic
├── requirements.txt - dependencies
│
├── tests/
│   └── test_cypher.py - pytest
│
├── templates/
│   └── index.html - html page
│
└── static/
    └── style.css - styles
```

## Setup
- ```git clone https://github.com/evlit69/SE_5```
- ```cd SE_5```  
- ```python3 -m venv venv```
- ```source venv/bin/activate```
- ```pip install -r requirements.txt```
- ```python app.py```

## Dependencies
- Flask >= 3.0
- pytest >= 8.0
- mypy

## Run tests
```text
pytest -v
```

### Additional (For devs)
- ```ruff check .```
- ```mypy .```