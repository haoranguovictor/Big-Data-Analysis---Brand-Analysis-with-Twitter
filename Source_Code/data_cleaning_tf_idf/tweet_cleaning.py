# *************************************************
#                                                 *
#                Tweet Cleaning                   *
#                Team: BDII                       *
#                Course:EECS6893                  *
#               Columbia University               *
#                                                 *
# *************************************************

# *************************************************
# ****************Class tweet_cleanin**************
# *************************************************
class tweet_cleaning():
    def cleaning(self, data):
        import re
        from HTMLParser import HTMLParser
        import itertools

        original_tweet = data
# *************************************************
#******************HTML Parser*********************
# *************************************************
        
        html_parser = HTMLParser.HTMLParser()
        tweet_htmlparsed = html_parser.unescape(original_tweet)

# *************************************************       
#******************Decoding Data*******************
# *************************************************
        
        tweet_decoded = data.encode('ascii', 'ignore').decode("utf8")

# *************************************************        
#******************Apostrophe Lookup***************
# *************************************************
        
        APPOSTOPHES = {"'s":"is", "re":"are", "'m": "am"}#more words could be added
        words = tweet_decoded.split()
        tweet_apostrophe_done = " ".join([APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words])

# *************************************************
#******************Split Attached Words************
# *************************************************

        tweet_attachedwords_done = " ".join(re.findall('[A-Z][^A-Z]*',tweet_apostrophe_done))

# *************************************************
#******************Standardizing Words*************
# *************************************************
        
        tweet_standard = "".join("".join(s)[:2] for _, s in itertools.groupby(tweet_apostrophe_done))
        
# *************************************************
#******************Removal of URLs*****************
# *************************************************

        tweet_nourls = re.sub(r'http\S+', '', tweet_standard)
        tweet_nourls2 = re.sub(r'\S+com', '', tweet_nourls)

# *************************************************        
#******************Convert to Lower Case***********
# *************************************************

        tweet_lower = tweet_nourls2.lower()

        return tweet_lower
# *************************************************
# ********A simple test for tweet cleanning********
# *************************************************

if __name__=="__main__":
    obj=tweet_cleaning()
    x = obj.cleaning("AttachWordIsMe 's fine, but I 'm had trouble taking it 's seriously after the beginning, https://www.analyticsvidhya.com/blog/ www.analyticsvidhya.com/blog/")
    print(x)
