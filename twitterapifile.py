from tweepy import Stream
from TwitterAPI import TwitterAPI
import json
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time


ckey=''#Consumer Key
csecret=''#Consumer Secret
atoken=''#Access token
asecret=''#Access Secret
api = TwitterAPI(ckey, csecret, atoken, asecret)

class listener(StreamListener):
    def on_data(self,data):
        try:
           
            print data
            saveFile=open('NYData.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True 
        except BaseException,e:
                print'failed ondata,',str(e)
                time.sleep(5)
        
    def on_error(self,status):
        print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
tweets = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
twitterStream.filter(track=["traffic"])

