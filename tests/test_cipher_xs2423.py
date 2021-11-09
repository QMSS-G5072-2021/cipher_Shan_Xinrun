from cipher_xs2423 import cipher_xs2423

import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert isinstance(shift, int), 'The shift parameter should be an integer'
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_single():
    example1 = 'selina'
    expected1 = 'tfmjob'
    actual1 = cipher(example1, 1)
    assert actual1 == expected1,'Cipher function is not working as expected for single words'
    
def test_cipher_negative():
    example2 = 'routine'
    expected2 = 'qntshmd'
    actual2 = cipher(example2, -1)
    assert actual2 == expected2,'Cipher function is not working as expected for negative shifts'

def test_cipher_nonalphabet():
    example3 = 'selina!'
    expected = 'tfmjob!'
    actual = cipher(example3, 1)
    assert actual == expected,'Cipher function is not working as expected for non-alphabetical symbols'
   
def test_cipher_shift():
    with pytest.raises(AssertionError):
        cipher('Selina','two',encrypt = True)   
