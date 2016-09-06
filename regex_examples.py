
""" Intro. to RegEx module based on examples at
    "https://en.wikipedia.org/wiki/Regular_expression#Examples"
"""

import re

string = "Hello World"

for i in range( 11 + 1 ):

    if i == 0: pattern = r"....."
    elif i == 1: pattern = r"(H..).(o.)"
    elif i == 2: pattern = r"l+"    
    elif i == 3: pattern = r"H.?e"
    elif i == 4: pattern = r"(l.+?o)"
    elif i == 5: pattern = r"el*o"
    elif i == 6: pattern = r"l{1,2}"
    elif i == 7: pattern = r"[aeiou]+"
    elif i == 8: pattern = r"(Hello|Hi|Pogo)"
    elif i == 9: pattern = r"llo\b"
    elif i == 10: pattern = r"\w"
    elif i == 11: pattern = r"\W"

    if bool( re.search( pattern, string ) ):
        if i == 0: message = "'%s' has length >=5." % string
        elif i == 1: message = "We matched '%s' and '%s'." % ( re.split( pattern, string )[ 1 ], re.split( pattern, string )[ 2 ])            
        elif i == 2: message = "There are one or more consecutive letter l's in '%s'." % string
        elif i == 3: message = "There is an 'H' and a 'e' separated by 0-1 characters (e.g., He Hue Hee)."
        elif i == 4: message = "The non-greedy match with 'l' followed by one or more characters is 'llo' rather than 'llo Wo'."
        elif i == 5: message = "There is an 'e' followed by zero to many 'l' followed by 'o' (e.g., eo, elo, ello, elllo)."
        elif i == 6: message = "There exists a substring with at least 1 and at most 2 l's in '%s'" % string
        elif i == 7: message = "'%s' contains one or more vowels." % string
        elif i == 8: message = "'%s' contains at least one of Hello, Hi, or Pogo." % string
        elif i == 9: message = "There is a word that ends with 'llo'."
        elif i == 10: message = "There is at least one alphanumeric character in '%s' (A-Z, a-z, 0-9, _)." % string
        elif i == 11: message = "The space between Hello and World is not alphanumeric."

        print( message )

