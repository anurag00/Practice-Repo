import tweepy

#read token file
a=[]
with open("/home/user/Desktop/Anurag/Code/ApiToken.txt",'r') as file:
    for line in file:
        a.append(line.strip())
file.close()
print("Authenticating user...")
#print("Consumer key = {0}\nConsumer secret key = {1}\nAccess token = {2}\nAccess token sceret = {3}".format(a[0],a[1],a[2],a[3]))

#creating tweepy API
auth = tweepy.OAuthHandler(a[0],a[1])
auth.set_access_token(a[2],a[3])
api = tweepy.API(auth)

#selecting the user
user = "realDonaldTrump"

#query for timeline using status.user_timeline
results = api.user_timeline(screen_name = user,count = 5, tweet_mode = 'extended')

#print results
with open("/home/user/Desktop/Anurag/Code/Output.txt",'w') as file2:
    for tweet in results:
        if tweet['retweeted_status']:
            file2.write(tweet['retweeted_status']['full_text'])
            file2.write("\n\n")
            continue
        try:
            file2.write(tweet.full_text)
        except Exception as e:
            file2.write(tweet.text)
        file2.write("\n\n")
file2.close()

print("Data saved in file...")