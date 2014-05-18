"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import hashlib
import random
from sys import version_info as version

hashfunc_dic = {"md5":hashlib.md5, "sha224": hashlib.sha224, "sha256":hashlib.sha256, "sha256":hashlib.sha256,
            "sha384":hashlib.sha384, "sha512":hashlib.sha512, "sha1":hashlib.sha1
            }


if version.major == 3:
    hash_text = lambda t, func: hashfunc_dic[func](bytes(t, "utf-8")).hexdigest()
else:
    hash_text = lambda t, func: hashfunc_dic[func](t).hexdigest()

result_list = []
for hash_f in hashfunc_dic:
    for i in range(40):
        t=""
        for j in range(1, random.randint(1,100)):
            t+=chr(random.randint(32,126))
        result_list.append({"input": (t, hash_f), "answer": hash_text(t, hash_f)})

TESTS = {
    "Basics": [
        {
            "input": ('welcome to pycon','md5'),
            "answer": hash_text('welcome to pycon','md5')
        },
        {
            "input": ('welcome to pycon', 'sha224'),
            "answer": hash_text('welcome to pycon','sha224')
        },
        {
            "input": ('welcome to pycon', 'sha256'),
            "answer": hash_text('welcome to pycon','sha256')
        },
        {
            "input": ('welcome to pycon', 'sha384'),
            "answer": hash_text('welcome to pycon','sha384')
        },
        {
            "input": ('welcome to pycon', 'sha512'),
            "answer": hash_text('welcome to pycon','sha512')
        },
        {
            "input": ('welcome to pycon', 'sha1'),
            "answer": hash_text('welcome to pycon','sha1')
        }

    ],
    "Extra": result_list
    }
