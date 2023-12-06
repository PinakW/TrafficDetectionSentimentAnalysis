from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey=''#Consumer Key
csecret=''#Consumer Secret
atoken=''#Access token
asecret=''#Access Secret

class listener(StreamListener):
    def on_data(self,data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]#[1] Will give the body of the text msg .i.e. everything right to the word text
            print tweet
            saveThis = tweet
            saveFile=open('twitDataBaseFiltered.csv','a')
            saveFile.write(saveThis)
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
twitterStream.filter(track=["traffic"])
