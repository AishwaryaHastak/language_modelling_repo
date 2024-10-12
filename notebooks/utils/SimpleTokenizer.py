# SimpleTokenizer.py

import re
class SimpleTokenizer:
    def __init__(self, vocab):
        """
        Initialize a SimpleTokenizer object.

        Args:
            vocab (dict): A dictionary with words as keys and their corresponding IDs as values.
        """
        self.vocab = vocab
        self.reverse_lookup = {i: w for w, i in vocab.items()}

    def encode(self, text):
        """
        Encode a given text into a list of token IDs.

        Args:
            text (str): The text to be encoded.

        Returns:
            list: A list of token IDs corresponding to the input text.
        """
        tokens = re.split(r'([,.:;?_!"()\'-])|\s', text)
        # Filter out empty strings
        tokens = [token for token in tokens if token]
        return [self.vocab[token] if token in self.vocab else self.vocab['<|UNK|>'] for token in tokens]

    def decode(self, tokens):
        """
        Decode a list of token IDs into a string.

        Args:
            tokens (list): A list of token IDs.

        Returns:
            str: The decoded string.
        """
        return ' '.join([self.reverse_lookup[token] for token in tokens])