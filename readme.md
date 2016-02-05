This is the code supplement to [this article]().

Instructions for running:
==

To get the vecs, I use the Python wrapper of word2vec ([here](https://github.com/danielfrg/word2vec)) with these settings, on Brown corpus catted to one file in `corpus.txt`:

```
word2vec -train corpus.txt -output vecs.txt -size 10
```

Then, just run process.py.
