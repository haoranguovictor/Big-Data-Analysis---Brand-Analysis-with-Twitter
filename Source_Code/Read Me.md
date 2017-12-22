# Read Me
1.File tweet_crawl contains source code for crawling tweets from internet, this part is from https://github.com/Jefferson-Henrique/GetOldTweets-python
2.Directory data_cleaning_tf_idf contains two python files. 
tweet_cleaning.py is used for cleaning raw twitter data and make them standardized and easy for future use.
tfidf_count.py is used for calculating tf-idf in different files. It would import tweet_cleaning.py for tweet data. In order to suit for twitter data, this part is modified from http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
3.Directory sentiment_analysis contains a ipython notebook. This part is implemented in databricks, connected with AWS. Using pyspark to train an sentiment classifier and do sentiment prediction for tweets we scrawled.
4.Directory visualization_code contains several ipython notebooks. These python codes do visualization on tweets.

