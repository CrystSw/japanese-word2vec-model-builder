Japanese Word2Vec Model Builder
===============================

A tool for building gensim word2vec model for Japanese.

It uses Sudachi for tokenization.
Wikipedia is used as a corpus for training word2vec model.

Requirements
------------

+ cURL
+ Python == 3.7

Setup
-----

```
python3 -m venv .env
. .env/bin/activate
pip3 install -r requirements.txt
```

Run
---

An example to build a model at the default path. (output/word2vec.gensim.model)

```
. .env/bin/activate
./build --download-wikipedia-dump --build-gensim-model
```

Another example to specify hyper parameters.

```
. .env/bin/activate
./build -o output/another.model --build-gensim-model --size=50 --window=10 --min-count=5
```

How to use the model
--------------------

```
from gensim.models.word2vec import Word2Vec

model_path = 'output/word2vec.gensim.model'
model = Word2Vec.load(model_path)
```
