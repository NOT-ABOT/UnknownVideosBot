import praw, time, sqlite3, re


#######################################################################################
#This needs to be filled in on your own and should never be shown to anyone           #
#######################################################################################

user_agent = ''
app_id = ''
app_secret = ''
app_uri = ''
app_scopes = ''
refresh_token = ''


def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(refresh_token)
    return r


disclaimer = '''\n\n
*I am a bot. If you have any questions or concerns regarding the actions of this bot, or feel that this was done in error,
 [please message the moderators](https://www.reddit.com/message/compose?to=%2Fr%2Funknownvideos).
 If you would like a bot of your own, feel free to [message the creator of this bot](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)'''
removal_message = 'This post has been deleted due to the fact that you have posted more than four comments this month from '
sub = 'unknownvideos'
usernames = ['example_username',
             ''] #List the moderators or people you would like to exempt from this bot. Include the bot's username and exclude the /u/
mod = 'jontheboss'
title ='Found a overposter'
maxposts = 500
url = ['https://www.youtube.com',
       'https://www.reddit.com']  #A list of sites that you use/allow on your sub. The ones here are just examples

print('Retrieving Database...')
database = sqlite3.connect('database.db'):
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()



def search_posts(): #Searches for the posts on your sub
    submissions = r.get_subreddit(sub).get_new(limit=maxposts)
    for submission in submissions:
        cur.execute('SELECT * FROM answered WHERE ID=?', [submission.id])
        if not cur.fetchone(): #Will only respond to
            try:
                author = submission.author.name
                if author != any(username in usernames): #Checks to make sure that it is not responding to a mod or itself
                    submission_title = submission.url
                    submission_text = submission.body.lower()
                    for i in range(len(urls)):
                        if re.match(url[i], submission_title) or re.match(url[i], submission_text):
                            user = r.get_user(author) #get's the user
                            user_submissions = user.get_submitted(limit=10, sort=top, ).url
                            for x in range(20):
                                check = len(re.findall(url[x], user_submissions))
                                if check > 4:
                                    r.send_message(mod, title, '/u/'+author+' may be breaking the rules. I have deleted his/her more recent post. [You might want to check it out]('+submission)
                                    submission.add_comment(removal_message + disclaimer)
                                    submission.delete
                        else:
                            pass
            except AttributeError: #Checks if post has been deleted and skips it if it has
                pass

r
load = 1
while True:
    search_posts()
    time.sleep(2) #You can only request every two seconds
    load += 1
    if load == 1800:
        r
