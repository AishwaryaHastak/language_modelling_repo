# generate_vocab.py

import re

def generate_vocab(text):
    """
    Generate a vocabulary from a given text.

    Parameters
    ----------
    text : str
        The text to generate the vocabulary from.

    Returns
    -------
    vocab : dict
        A dictionary with words as keys and their indices as values.

    Notes
    -----
    The generated vocabulary will include the special tokens <|EOS|> and <|UNK|>, which
    are used to indicate the end of a sequence and unknown words, respectively.
    """
    words = re.split(r'([,.:;?_!"()\'-])|\s', text)

    # Filter out empty strings
    words = [word for word in words if word]

    unique_words = list(set(words))
    special_tokens = ["<|EOS|>", "<|UNK|>"]
    unique_words.extend(special_tokens)
    vocab = {word: index for index, word in enumerate(unique_words)}
    
    return vocab