from sudachipy import tokenizer
from sudachipy import dictionary


def get_tokenizer_obj():
    return dictionary.Dictionary(dict_type="full").create()


def tokenize(text, tokenizer_obj):
    tokens = []
    for t in text.split('\n'):
        if len(bytes(t, 'utf-8')) >= 49149:
            print("Cannot split token because string is too long. This string will be skipped: " + t)
            continue
        for m in tokenizer_obj.tokenize(t, tokenizer.Tokenizer.SplitMode.A):
            tokens.append(m.normalized_form())
    return tokens
