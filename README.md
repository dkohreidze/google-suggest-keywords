# google-suggest-keywords

####`googleSuggest.py`

This script queries Google and returns a list of suggested keywords (from Google Instant Search results) based on the input keywords.

This URL is queried to obtain the Instant Search results: http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&q=keyword. 

The URL outputs an XML file that contains the top 10 suggested keywords based on the input keyword (`?q=keyword`). These keyword suggestions come directly from Google Instant Search results. The keyword suggestions are then parsed out of the XML file and simply returned into your Terminal.

Any number of keywords are accepted as keywords in the script. The input keywords must be enumerated directly into the code, contained in a Python dictionary data structure. 

Please note: While any number of keywords are able to be queried, too frequent queries to this URL could trigger a permanent IP ban from Google. Once banned it's a long and difficult process to get your IP unbanned so proceed with caution.
