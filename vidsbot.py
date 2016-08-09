import praw, time, sqlite3, re


#######################################################################################
#This needs to be filled in on your own and should never be shown to anyone           #
#######################################################################################


print('Logging in to Reddit as /u/UnknownVideosMod...')

def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(refresh_token)
    return r
r = login()
r

disclaimer = '''\n\n
*I am a bot. If you have any questions or concerns regarding the actions of this bot, or feel that this was done in error,
 [please message the moderators](https://www.reddit.com/message/compose?to=%2Fr%2Funknownvideos).
 If you would like a bot of your own, feel free to [message the creator of this bot](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)*'''
removal_message = 'This post has been deleted due to the fact that you have posted more than once this week from this domain. Please post from a variety sources. Thanks!'
sub = 'unknownvideos_test'
username = 'UnknownVideosMod'

usernames = ['___NOT_A_BOT___',
             'UnknownVideosMod',
             'jontheboss']

mod = 'jontheboss'
title ='Found a overposter'
maxposts = 500
urls = ['https://www.y(.*)e.com',
       'https://i(.*)r.com',]

print('Retrieving Database...')
database = sqlite3.connect('database.db')
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()

def clock(): #Adding a clock function Here
    now = localtime(time.time())
    print(now[5])

def search_posts(): #Searches for the posts on your sub
    submissions = r.get_subreddit(sub).get_new(limit=maxposts)
    for submission in submissions:
        if submission.author.name == None:
            continue
        cur.execute('SELECT * FROM answered WHERE ID=?', [submission.id])
        if not cur.fetchone():
            author = submission.author.name.lower()
            for n in range(len(usernames)):
                if not re.match(usernames[n].lower(), author):
                    submission_url = submission.url
                    for i in range(len(urls)):
                        if re.match(urls[i], submission_url):
                            cur.execute('INSERT INTO answered VALUES(?)', [submission.id])
                            database.commit()
                            user_submissions = r.get_redditor(author).get_submitted(limit=10)
                            for user_submission in user_submissions:
                                if re.findall(urls[i], user_submission.url) > 1 and user_submission in sub:
                                    r.send_message(mod, title, '/u/'+author+' may be breaking the rules. I have deleted his/her most recent post. [You might want to check it out]('+str(submission))
                                    r.send_message(author, 'Private Message', 'Between you and me, I disagree with what those evil humans made me do.') #This is just for fun
                                    print('Removing potential rulebreaker')
                                    submission.add_comment(removal_message + disclaimer)
                                    submission.delete


load = 1
while True:
    print('Parsing Submissions...')
    search_posts()
    time.sleep(2)
    load += 1
    if load == 1000:
        r
