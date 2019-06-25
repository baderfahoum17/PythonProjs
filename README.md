# DictionaryApp
as a side mission of a bigger project, an working simple Dictionary app in python


process of making
#### 1)
to load the data from the data.json

run in the Terminal:
```
$ python
this is a default python library so no need to install external packages
import json 
to better get a hold(understanding) of this lib run help
help(json.load)
```
data = json.load(open("path/to/file-like-object-containing a JSON document"))
```
[baderf@ ~InteractiveDictionary]$ python3
>>> import json
>>> help(json.load)
>>> data = json.load(open("data.json"))
>>> type(data)
<class 'dict'>
```
#### 2) 
to spice our Dictionary app further
we want to suggest similar word to the user if the user has a typo maybe
the SequenceMatcher Class within difflib package can help us do just that :) 

run in terminal:
```
[baderf@ ~InteractiveDictionary]$ python3
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import difflib
>>> from difflib import SequenceMatcher
>>> help(SequenceMatcher)
	class SequenceMatcher(builtins.object)
	 |  SequenceMatcher(isjunk=None, a='', b='', autojunk=True)
>>> SequenceMatcher(None, "rainn", "rain")
<difflib.SequenceMatcher object at 0x109c8c4e0>
>>> SequenceMatcher(None, "rainn", "rain").ratio()
0.8888888888888888 
```
#### 3) 
a method in SequenceMatcher which is very useful here is get_close_matches()


so lets import it!
```
>>> from difflib import get_close_matches
>>> help(get_close_matches)
man page:
get_close_matches(word, possibilities, n=3, cutoff=0.6)
    Use SequenceMatcher to return list of the best "good enough" matches.

usage example:
>>> get_close_matches("waterfall", ["rain","eurozone","waterfall"])
['waterfall']
```
#### 4) 
now lets try to apply it on our json database!

using data.keys() will provide us will all the key values of our dictionary which is loaded into our data variable
```
>>> get_close_matches("waterfall", data.keys())
['waterfall', 'waterlily', 'waterfowl']
```
we can load more closely related words with :
```
>>> get_close_matches("waterfall", data.keys(), n=5)
['waterfall', 'waterlily', 'waterfowl', 'lateral', 'water well']
```
the results are sorted via the ratio() we saw earlier
so the first word will always be the closest matching word

so if a typo has occured while entering the search word like typing watorfalll (with an extra L): 
```
>>> get_close_matches("waterfalll", data.keys(), n=5)
['waterfall', 'waterlily', 'waterfowl', 'lateral', 'water well']
```
we can grab the first index to get the closest match
example:
```
>>> get_close_matches("watorfalle", data.keys())[0]
'waterfall'
>>> get_close_matches("watorfalll", data.keys())[0]
'waterfall'
```





