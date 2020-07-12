# eos_app
Project provides functionality for manipulate data received from stdin. Namely saving array to file. 

### Tech
Requires Python 3.8 to run.

### Tests
```sh
python3.8 -m unittest src/tests/all_tests.py
```
Wait while it will say OK

### Run
```sh
src/main.py "path/to/file.json" "[[1,2],[3,4],[5,6]]"
```
At the moment exists maintenance of following extensions: .json .csv
