def cipher(text, shift, encrypt=True):
    
    """
    This is a package to encipher the input.

    Parameters
    ----------
    text: a sequence of string
    shift: an integer number of shifts
    encrypt: boolean value True or False

    Returns
    -------
    encrypted string

    Examples
    --------
    >>> from cipher_xs2423 import cipher_xs2423
    >>> text = 'abcde'
    >>> shift = 1
    >>> cipher_xs2423.cipher(text,shift）
    ‘bcdef'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
