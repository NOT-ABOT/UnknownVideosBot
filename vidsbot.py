import praw, time, sqlite3, re


#######################################################################################
#This needs to be filled in on your own and should never be shown to anyone           #
#######################################################################################



def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(refresh_token)
    return r
r = login()
r


disclaimer = '''\n\n-----------------------------------------------------------------------------------------------------------\n\n
*I am a bot, and this was done automatically. If you have any questions or concerns regarding the actions of this bot, or feel that this was done in error,
 [please message the moderators](https://www.reddit.com/message/compose?to=%2Fr%2Funknownvideos).
 If you would like a bot of your own, feel free to [message the creator of this bot](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)*'''
removal_message = 'This post has been deleted due to the fact that you have posted more than once this week from this domain. Please post from a variety sources. Thanks!'
sub = 'unknownvideos_test'
username = 'UnknownVideosMod'

usernames = [
             'unknownvideosmod',
             'jontheboss']

mod = 'jontheboss'
title ='Found a overposter'
maxposts = 500
urls = ['https://www.youtube.com/user/(.*)',
        'https://www/youtu.be.com/user/(.*)',
       'https://imgur.com',]

print('Retrieving Database...')
database = sqlite3.connect('database.db')
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()


def save():
    cur.execute('INSERT INTO answered VALUES(?)', [submission.id])
    database.commit()

def get_submissions():
    submissions = r.get_subreddit(sub).get_new(limit=maxposts)
    for submission in submissions:
        if submission.author.name == None:
            continue
        cur.execute('SELECT * FROM answered WHERE ID=?', [submission.id])
        if not cur.fetchone():
            author = submission.author.name.lower()

def remove_post():
    r.send_message(mod, title, '/u/'+author+' may be breaking the rules. I have deleted the submission, but you should still check it out.')
    r.send_message(author, 'I\'m sorry', 'I disagree with what those evil humans made me do!')
    submission.add_comment(removal_message + disclaimer)
    submission.remove()

def search_user():
    user_submissions = r.get_redditor(author).get_submitted(limit=10)
    for user_submission in user_submissions:
        if len(re.findall(urls[i], user_submission.url)) > 1:
            remove_post()
            
def check_for_mods():
    for n in range(len(usernames)):
        return False if not re.match(usernames[n], author)
            
            
def search_posts():
    get_submissions()
    check_for_mods()
    if check_for_mods == False:
            for i in range(len(urls)):
                if re.match(urls[i], submission.url):
                    save()
                    search_user()

load = 1
while True:
    print('Parsing Submissions...')
    search_posts()
    time.sleep(2)
    load += 1
    if load == 1000:
        r
