1. install requirements. E.g.
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. run tests using pytest. E.g.
   ```
   python -m pytest
   ```

   using the verbose (`-v`) flag shows individual test names in the output
   ```
   python -m pytest -v
   ```

   the pytest-spec plugin renders fancy output and shows comments in the test
   ```
   python -m pytest --spec
   ```