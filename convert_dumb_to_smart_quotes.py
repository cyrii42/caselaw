import re
from pathlib import Path

def dumb_to_smart_quotes(string):
    ### Found at https://gist.github.com/davidtheclark/5521432
    """Takes a string and returns it with dumb quotes, single and double,
    replaced by smart quotes. Accounts for the possibility of HTML tags
    within the string."""

    # Find dumb double quotes coming directly after letters or punctuation,
    # and replace them with right double quotes.
    string = re.sub(r'([a-zA-Z0-9.,?!;:\'\"])"', r'\1&#8221;', string)
    # Find any remaining dumb double quotes and replace them with
    # left double quotes.
    string = string.replace('"', '&#8220;')
    # Reverse: Find any SMART quotes that have been (mistakenly) placed around HTML
    # attributes (following =) and replace them with dumb quotes.
    string = re.sub(r'=&#8220;(.*?)&#8221;', r'="\1"', string)
    # Follow the same process with dumb/smart single quotes
    string = re.sub(r"([a-zA-Z0-9.,?!;:\"\'])'", r'\1&#8217;', string)
    string = string.replace("'", '&#8216;')
    string = re.sub(r'=&#8216;(.*?)&#8217;', r"='\1'", string)
    return string

def dumb_to_smart_quotes_v2(string):
    """Takes a string and returns it with dumb quotes, single and double,
    replaced by smart quotes. Accounts for the possibility of HTML tags
    within the string."""

    # Find dumb double quotes coming directly after letters or punctuation,
    # and replace them with right double quotes.
    string = re.sub(r'([a-zA-Z0-9.,?!;:\'\"])"', r'\1”', string)
    # Find any remaining dumb double quotes and replace them with
    # left double quotes.
    string = string.replace('"', '“')
    # Reverse: Find any SMART quotes that have been (mistakenly) placed around HTML
    # attributes (following =) and replace them with dumb quotes.
    string = re.sub(r'=“(.*?)”', r'="\1"', string)
    # Follow the same process with dumb/smart single quotes
    string = re.sub(r"([a-zA-Z0-9.,?!;:\"\'])'", r'\1’', string)
    string = string.replace("'", '‘')
    string = re.sub(r'=‘(.*?)’', r"='\1'", string)
    return string

# fcra_dir = Path('./docs/fcra')
# for i, file in enumerate(fcra_dir.iterdir()):
#     with open(file) as f:
#         text = f.read()
#         new_text = dumb_to_smart_quotes_v2(text)

#     with open(f"{i}.md", "w") as f:
#         f.write(new_text)