# What is this?
This is an extension to eng-to-ipa. Basically I wanted a module that could give me the IPA of an English word, and also the corresponding English word for some IPA word.

## Dependencies
1. eng-to-ipa
2. https://github.com/dwyl/english-words
3. tqdm

## How do I install this library?
1. first install the eng-to-ipa library
2. next, make a data directory, and inside it, clone the english-words repo
3. now, run `python prep.py`
4. now, to use the functions listed in util.py as a library, you must include the path to this directory in your PYTHON_PATH, or in python, the sys.path variable