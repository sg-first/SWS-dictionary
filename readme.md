SWS dictionary
============
stopWords
-------------
This is a stop words dictionary. Using its API, you can find out whether a word is a stop word quickly.
### API list
Import `stop.py` you can use API of the lib.
* `init(dictionary path)` After calling the function, you can use the lib.
* `isStopWord(word)` Finding out whether a word is a stop word.
### Building Dictionaries
Add your stop words to `stopWordList(sou).txt` (Dividing with newline). Then run `genStop.py`, Machine-Readable dictionary will be built.

Synonyms
--------------
A Machine-Readable dictionary of synonyms. Using its API, you can calculate the distance between two words quickly or directly determine whether two words are synonyms after setting thresholds. The dictionary is constructed based on `Õ¨“Â¥ ¥ ¡÷`.
### API list
Import `synonyms.py` you can use API of the lib.
* `init(dictionary path)` After calling the function, you can use the lib.
* `getid(word)` Get the distance ID of a word in the dictionary.
* `getDistance(word1,word2)` Get the word meaning distance of two words.
* `isSynonyms(word1,word2,threshold=0)` Query whether two words are synonyms (meaning distance is less than threshold value).
### Building Dictionaries
Add your words and its distance ID to `synonymsList(sou).txt` (Dividing ID and word with comma, dividing word with newline). Then run `genSynonyms.py`, Machine-Readable dictionary will be built.
