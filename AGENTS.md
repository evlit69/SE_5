# AGENTS.md
___
## Project
Caesar Cipher Python Web Application.  
Users can encrypt and decrypt messages;  
There is no login and database;  
All data is in-memory;  

## Structure
```text
SE_5/
├── app.py - main app logic
├── cipher.py - cipher logic
├── requirements.txt - dependencies
│
├── tests/
│   └── test_*cypher*.py - vitest
│
├── templates/
│   └── index.html - html page
│
└── static/
    └── style.css - styles
```
## Installation

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run application
```
python app.py
```
## Testing
- Test framework: Pytest
- Run all tests:
```text
pytest -v
```
- Verify that all tests passed

## Forbidden actions
- No database implementation 
- No login
- Forbidden commands:
  - ```rm -rf```
  - ```git push --force```
  - ```reset --hard```

## Agent instructions
- Inspect the existing code before making changes;
- Keep changes within the current project scope;
- Do not introduce a database, authentication, or persistent storage;
- Run relevant tests after modifying the code;
- Do not modify test expectations just to make failing tests pass;