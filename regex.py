"""Regular expressions.

Operators

^ -> Start of the string (include immediatly after each newline, in MULTILINE mode)
$ -> End of the string (include newline in MULTILINE mode)
. -> Any character except newline (include newline in DOTALL mode)
* -> 0 or more repetitions of the preceeding RE
+ -> 1 or more repetitions of the preceeding RE
? -> 0 or 1 repetition of the preceeding RE
"""

import re

def validate_date(date: str) -> bool:
    """
    Validate date with regex.

    Parameters
    ----------
        date
            A date string in the format yyyy-mm-ddTHH:MM:SS
    
    Return
        True or False.
    """
    pattern = r'(1\d{3}|2\d{3})-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9]:[0-5][0-9]'

    is_valid = re.fullmatch(pattern, date)

    return True if is_valid else False


if __name__ == "__main__":
    email = 'marcelo.coelho@email.com'
    pattern = '([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2, })+'










    date = '3023-11-01T20:50:00'
    email_pattern = '([a-z0-9]+[.-_])*[A-Za-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+'

    print(validate_date(date))
    

