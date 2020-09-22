"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""
# >>> compress('aabbaabc')
# 'a2b2a2b2'
#We can not use dictionary because it has no order.
    res=[]
    count=1
    res.append(string[0])
    for i  in range(len(string)-1):

        if string[i] == string[i+1]:
                count= count+1
        else:
            if count >1:
                res.append(count)
                count=1
            res.append(string[i+1])
    #a2b2a2bc
    if count>1:
        res.append(count)

    return ''.join(map(str,res))
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
