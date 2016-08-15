import praw, time, sqlite3, re

def login():
    print('Logging in to Reddit as /u/UnknownVideosMod...')
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
             'unknownvideosmod',]

urls = ['https://www.youtube.com',
        'https://www/youtu.be.com',
       'https://imgur.com',]

print('Retrieving Database...')
database = sqlite3.connect('database.db')
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()

def get_submissions(sub='unknownvideos_test', posts=100):
    submissions = r.get_subreddit(sub).get_new(limit=posts)
    for submission in submissions:
        if submission.author.name == None:
            continue
        cur.execute('SELECT * FROM answered WHERE ID=?', [submission.id])
        if not cur.fetchone():
            author = submission.author.name.lower()

def send(mod='jontheboss', title='Potential Rulebreaker', message='/u/'+author+' may be breaking the rules. [You should check it out]('+str(submission.url)+')'):
    r.send_message(mod, title, message)


def search_posts():
    get_submissions()
    if not re.match(usernames[n], author) and not any(urls in submission.url):
        #cur.execute('INSERT INTO answered VALUES(?)', [submission.id])
        #database.commit()
        user_submissions = r.get_redditor(author).get_submitted(limit=10)
        for user_submission in user_submissions:
            if len(re.findall(urls[i], user_submission.url))  > 1:
                send()
                print('Removing potential rulebreaker')
                submission.add_comment(removal_message + disclaimer)
                submission.remove()



load = 1
while True:
    print('Parsing Submissions...')
    search_posts()
    time.sleep(2)
    load += 1
    if load == 1000:
        r
