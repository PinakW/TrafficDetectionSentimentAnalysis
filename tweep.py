from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey='dJKr0gXQcRJSZ0hsuUTXf5WLf'#Consumer Key
csecret='S0hkHAZHmVjLtIO1vS0l3boUDoffhT5CpNxejtK9pLztwgd0sA'#Consumer Secret
atoken='2964019449-aIqNFXacvdvivZxRmyGcsSR1ncHqgSXYunrde5D'#Access token
asecret='iptPkPvBUQyog6eA6aoMNQZv1gxC3SUgUY0Yj0leejE9b'#Access Secret

class listener(StreamListener):
    def on_data(self,data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]#[1] Will give the body of the text msg .i.e. everything right to the word text
            print tweet
            saveThis = tweet
            saveFile=open('RealTimeTwitterData.csv','a')
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
