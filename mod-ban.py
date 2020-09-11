#!/usr/bin/python
# pastebin link: https://pastebin.com/UT7AYWZu
 
import praw
import sys
import pprint
import re
import sys
import codecs
 
permamute_users=["user1","user2"]
 
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
 
reddit=praw.Reddit(PRAW_INSTANCE_GOES_HERE)
conversations = reddit.subreddit('all').modmail.conversations()
for conversation in conversations:
	print conversation
	for author in conversation.authors:
		print author
		if author in permamute_users:
			conversation.mute()
			conversation.archive()
			message="%s is being muted in %s"%(author,conversation.id)
			print message
#			reddit.redditor(YOUR_USERNAME_HERE_FOR_NOTIFICATIONS).message('Permamute', message)
			break

<!--
# raw data
#!/usr/bin/python

import praw
import sys
import pprint
import re
import sys
import codecs

permamute_users=["user1","user2"]

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

reddit=praw.Reddit(PRAW_INSTANCE_GOES_HERE)
conversations = reddit.subreddit('all').modmail.conversations()
for conversation in conversations:
	print conversation
	for author in conversation.authors:
		print author
		if author in permamute_users:
			conversation.mute()
			conversation.archive()
			message="%s is being muted in %s"%(author,conversation.id)
			print message
#			reddit.redditor(YOUR_USERNAME_HERE_FOR_NOTIFICATIONS).message('Permamute', message)
			break-->
