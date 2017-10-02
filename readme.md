SWS dictionary
============
stopWords
-------------
This is a stop words dictionary. Using its API, you can find out whether a word is a stop word quickly.
### API list
Import °Æstop.py°Ø you can use API of the lib.
* °Æinit(dictionary path)°Ø After calling the function, you can use the lib.
* °ÆisStopWord(word)°Ø Finding out whether a word is a stop word.
### Building Dictionaries
Add your stop words to °ÆstopWordList(sou).txt°Ø (Dividing with newline). Then run °ÆgenStop.py°Ø, Machine-Readable dictionary will be built.

Synonyms
--------------
A Machine-Readable dictionary of synonyms. Using its API, you can calculate the distance between two words quickly or directly determine whether two words are synonyms after setting thresholds. The dictionary is constructed based on °ÆÕ¨“Â¥ ¥ ¡÷°Ø.
### API list
Import °Æsynonyms.py°Ø you can use API of the lib.
* °Æinit(dictionary path)°Ø After calling the function, you can use the lib.
* °Ægetid(word)°Ø Get the distance ID of a word in the dictionary.
* °ÆgetDistance(word1,word2)°Ø Get the word meaning distance of two words.
* °ÆisSynonyms(word1,word2,threshold=0)°Ø Query whether two words are synonyms (meaning distance is less than threshold value).
### Building Dictionaries
Add your words and its distance ID to °ÆsynonymsList(sou).txt°Ø (Dividing ID and word with comma, dividing word with newline). Then run °ÆgenSynonyms.py°Ø, Machine-Readable dictionary will be built.
