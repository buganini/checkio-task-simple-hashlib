"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import hashlib



TESTS = {
    "Basics": [
        {
            "input": ('welcome to pycon','md5'),
            "answer": hashlib.md5(b'welcome to simple pycon game').hexdigest()
        },
        {
            "input": ('welcome to pycon', 'sha224'),
            "answer": hashlib.sha224(b'welcome to pycon').hexdigest()
        },
        {
            "input": ('welcome to pycon', 'sha256'),
            "answer": hashlib.sha256(b'welcome to pycon').hexdigest()
        },
        {
            "input": ('welcome to pycon', 'sha384'),
            "answer": hashlib.sha384(b'welcome to pycon').hexdigest()
        },
        {
            "input": ('welcome to pycon', 'sha512'),
            "answer": hashlib.sha512(b'welcome to pycon').hexdigest()
        },
        {
            "input": ('welcome to pycon', 'sha1'),
            "answer": hashlib.sha1(b'welcome to pycon').hexdigest()
        }




    ]
    }
