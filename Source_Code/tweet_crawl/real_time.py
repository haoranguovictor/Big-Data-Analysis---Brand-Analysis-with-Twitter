# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


#Variables that contains the user credentials to access Twitter API
access_token = "930967187548004352-ESv1OyMW1bssEz3AEU1MqpjNM3entP2"
access_token_secret = "dyxiEYN0ZN60CzMb9pbzhmU4kZr5Sno1w85898QbNCAKq"
consumer_key = "EamTM57PCs8ubxEpPgh1fKiXb"
consumer_secret = "UODB9kr5VQu70RpYSyRB1LmZKGspZngbXVL6UjMmUURGsVWh4r"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        f = open('C:\Users\Mice\Desktop/bdpj/collection/realtime/data4.txt', 'a+')
        a=json.loads(data)
        print a["user"]["location"]
        f.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['coca cola'])

