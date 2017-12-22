

import got

def main():

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Example 1 - Get tweets by username
	#tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
	#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	#printTweet("### Example 1 - Get tweets by username [barackobama]", tweet)


	f = open('C:\Users\Mice\Desktop/bdpj/collection/final.txt', 'w')
	#Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('coca-cola').setSince("2017-12-01").setUntil("2017-12-12").setMaxTweets(150000)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)
	for xxy in tweet :
		f.write(xxy.hashtag+'\n')
	f.close()

	# Example 3 - Get tweets by username and bound dates
	#tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	#tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	#printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

if __name__ == '__main__':
	main()