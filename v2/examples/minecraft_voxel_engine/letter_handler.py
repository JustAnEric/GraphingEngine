from settings import LETTER_LISTINGS, njit
import os, json

@njit(cache=True)
def setup_characters():
    information = json.load(open('./assets/fonts/namespace.json'))
    for i in information:
        LETTER_LISTINGS.append(i)