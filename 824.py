
def toGoatLatin(self, S):
    """
    Translates a sentence to Goat Latin.

    Args:
        S (str): The sentence to translate.

    Returns:
        str: The translated sentence in Goat Latin.
    """
    vowel = set('aeiouAEIOU')
    def latin(w, i):
        if w[0] not in vowel:
            w = w[1:] + w[0]
        return w + 'ma' + 'a' * (i + 1)
    return ' '.join(latin(w, i) for i, w in enumerate(S.split()))


