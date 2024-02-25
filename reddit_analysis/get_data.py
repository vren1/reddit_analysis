import praw
reddit = praw.Reddit(
    client_id="Fgc3Muc1xyZVlDFiF2HKdw",
    client_secret="wU1t3tlKxglGFfICXItI0Mw6GSNsKg",
    user_agent="python:com.social-media-sentiment-app:v1.0.0 (by /u/iAmAwesome_10)",
    password='cats@2004',
    username='iAmAwesome_10'
)

# prints posts and replies to console
def extractCommentsAndReplies():
    for submission in reddit.subreddit("Turtles").hot(limit=1):
        print('\nOriginal Post: ')
        print(submission.title)
        print(submission.author)
        print(submission.selftext, '\n')
        print('Comments: ')
        submission.comments.replace_more()
        comments = submission.comments.list()
        for comment in comments:
            comment.refresh()
            print('Comment: ', comment.body, '\n')
            if comment.replies.list() != []:
                comment.replies.replace_more()
                replies = comment.replies.list()
                print('\nReplies:')
                for reply in replies:
                    print('\t',reply.body)

# returns posts in the form of iterable submissions
def extractPosts(topic, subreddit='all', number=500, time='year'):
    submissions = reddit.subreddit(subreddit).search(topic, limit=number, time_filter=time)
    return submissions