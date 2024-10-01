import re
from pathlib import Path

"""Changed smart-quote replacements as follows:
    - double: &#8220; to “
    - right double: &#8221; to ”
    - left single: &#8217; to ‘
    - right single: &#8216; to ’
"""

DOCS_PATH = Path('./docs')

def dumb_to_smart_quotes(string: str) -> str:
    """Takes a string and returns it with dumb quotes, single and double,
    replaced by smart quotes. Accounts for the possibility of HTML tags
    within the string.
    
    Adapted from https://gist.github.com/davidtheclark/5521432"""
    
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

def convert_quotes_in_markdown_docs() -> None:
    for file in DOCS_PATH.iterdir():  
        if file.suffix == 'md':
            with open(file, 'r') as f:
                text = f.read()
                new_text = dumb_to_smart_quotes(text)
            with open(file, 'w') as f:
                f.write(new_text)


def main():
    ...

if __name__ == '__main__':
    main()


# print("\N{LEFT DOUBLE QUOTATION MARK}")
# print("\N{RIGHT DOUBLE QUOTATION MARK}" == "”")

# test_str = '''
# #### Individualized Issues
# - [*Patel v. Trans Union, LLC*](https://www.westlaw.com/Document/I49d881801e5411e5be1ff4cec5913d5d/View/FullText.html?transitionType=Default&contextData=(sc.Default)&VR=3.0&RS=cblt1.0), 308 F.R.D. 292, 302 (N.D. Cal. 2015)
#   > The issue of accuracy is a core issue for ascertainability and the predominance of common issues. The defendants' fundamental quarrel is with the plaintiff's assertion that tagging the class members as (for example) 'terrorists' (via the name-only logic) is always inaccurate and thus is enough to define the class (and establish the predominance of this common issue). The defendants counter that the plaintiff cannot show, except file by file, that the SmartMove reports wrongly tagged the class members as terrorists. They complain that the plaintiff cannot just assert that the terrorist tags were inaccurate and then shift the burden to the defendants to prove that the tags were accurate.
#   > 
#   > Normally, the defendants would be right. But this case presents a peculiar situation. The defendants' implied argument is that a significant number of the proposed class actually may have been accurately tagged as potential terrorists. Absent some pretty significant proof to the contrary, the court is willing to assume that no significant (read: certification-breaking) fraction of the tagged proposed class was in fact accurately tagged as potential terrorists.

# #### Hypothetical scenarios

# - [*Van v. LLR, Inc.*](https://www.westlaw.com/Document/I8535be00c1d511edb30aae965a5264be/View/FullText.html?transitionType=Default&contextData=(sc.Default)&VR=3.0&RS=cblt1.0), 61 F.4th 1053, 1067-68 (9th Cir. 2023)
#   > ***If the plaintiff demonstrates that class issues exist, the defendant must invoke individualized issues and provide sufficient evidence that the individualized issues bar recovery on at least some claims, thus raising the spectre of class-member-by-class-member adjudication of the issue.*** See True Health Chiropractic, Inc. v. McKesson Corp., 896 F.3d 923, 932 (9th Cir. 2018) (“[W]e do not consider ... defenses that [the defendant] might advance or for which it has presented no evidence.” (emphasis added)).
#   >
#   > If the defendant provides evidence that a valid defense—affirmative or otherwise—will bar recovery on some claims, then the district court must determine, based on the particular facts of the case, “whether individualized questions ... ‘will overwhelm common ones and render class certification inappropriate under Rule 23(b)(3).’ ” Olean, 31 F.4th at 669 (quoting Halliburton Co. v. Erica P. John Fund, Inc., 573 U.S. 258, 276, 134 S.Ct. 2398, 189 L.Ed.2d 339 (2014))
#   >
#   > As pertains to the voluntary payment issue raised by LuLaRoe, LuLaRoe failed to provide sufficient evidence that any class member would lack a meritorious claim on this basis. Only a handful of Alaskan invoices submitted to the district court demonstrate that the purchaser knew of the sales tax issue before completing the purchase. And on each of these invoices, the purchaser was provided a discount on the transaction equal to or greater than the amount of improper sales tax, with at least some of the discounts provided for the express purpose of offsetting the sales tax.A nd, as discussed below, any purchaser who received a discount in an amount greater than or equal to the improper sales tax for the purpose of offsetting the sales tax never paid the improper tax at all.
#   > 
#   > Because these purchasers did not pay the sales tax, or at least their invoices do not demonstrate that they paid the sales tax, their invoices are not sufficient evidence that any class member knew of the sales tax and then paid it. The invoices, then, are not sufficient evidence that the individualized issue of voluntary payment bars recovery on at least some claims.
#   >
#   >The fashion retailer declarations suffer from the same problem. Although the declarations generally assert that some consumers across the country were told of the sales tax issue, the declarations do not state with certainty that any member of this Alaska class was informed of the nature of the improper sales tax, was not provided a discount, and paid the sales tax nonetheless.
#   >
#   >***We do not permit a defendant to support its invocation of individualized issues with mere speculation.*** See True Health, 896 F.3d at 932. LuLaRoe's scant evidence of voluntary payment is not sufficient to defeat predominance.

# - [*True Health Chiropractic, Inc. v. McKesson Corp.*](https://www.westlaw.com/Document/Ia19c2f8089df11e8a5b89e7029628dd3/View/FullText.html?transitionType=Default&contextData=(sc.Default)&VR=3.0&RS=cblt1.0), 896 F.3d 923, 931–32 (9th Cir. 2018) ("Since McKesson bears the burden [on its affirmative defense of consent], we assess predominance by analyzing the consent defenses McKesson has actually advanced and for which it has presented evidence. A defendant can produce evidence of a predominance-defeating consent defense in a variety of ways. But we do not consider the consent defenses that McKesson might advance or for which it has presented no evidence.")
# '''

# print(dumb_to_smart_quotes_v2(test_str))

# quote_str= '''
# '' " ＂ 〃 ˮ ײ ᳓ ″ ״ ‶ ˶ ʺ “ ” ˝ ‟
# '''

# for i, quote in enumerate(quote_str.replace(' ',''), start=1):
#     print(f"Symbol {i}: {quote}")
#     if quote == '“':
#         print(f"it's equal to {quote}, the {i}th one in the list")

# print('“' == '“')
# print('”' == '”')