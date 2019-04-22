# -*- coding: utf-8 -*-

import sys
import random
from time import sleep

import datetime
now = datetime.datetime.now()

feeling = ["hanging in there", "not okay", "really hurting right now"]
reason = ["I can easily recall", "it hurts to rememeber", "sometimes I still think about"]
sleeping = ["but don't worry about me, I’m okay now", "and I’m still struggling", "and now I’m having trouble sleeping alone"]
adjective = ["good", "terrible", "stupid"]
confession = ["I wish we could be close again", "I don't think we can be as close as before"]
you = ["just a friend", "like an acquaintance", "nothing"]
morefeelings = ["surprised", "happy", "sad"]
share = ["please tell me", "don’t tell me"]
outcome = ["we should have stayed together for a little longer to work it out", "it was a good idea for us to break up"]
decision = ["I want to see you one last time before you leave for New York", "I don’t think we should be in each other’s lives anymore"]

while True:
    print now.strftime("%Y-%m-%d %H:%M")
    print "Hi there."
    print "Thanks for checking in. Don\'t worry about me, I\'m %s but I\'ll be fine." % (random.choice(feeling))
    print "I know it\'s been a while since we last talked. I guess that\'s just strange to me because %s" % (random.choice(reason)) + " when we would see each other every single day."
    print "I don\'t know, I just got so used to having someone to come home to %s." % (random.choice(sleeping))
    print "I miss talking to you too. I admit though that giving each other space was a %s" % (random.choice(adjective)) + " idea."
    print "I\'ve thought about us. A lot. I don\'t consider us strangers — we still know each other very well, and I\'ve told you certain things about myself I would never tell anyone else."
    print "And %s," % (random.choice(confession)) + " but I won\'t do anything about that because I\'m just so tired of trying."
    print "I hate that I lost someone special to me. You used to be the most important person in my world, and now you\'re %s." % (random.choice(you))
    print "Honestly, I\'m %s" % (random.choice(morefeelings)) + " to know that you\'re seeing someone else, I heard about it yesterday and I didn\'t know what to think or say."
    print "Today I realized that I\'m still in love with you, and I know you don\'t need to know that but I wanted to tell you anyways."
    print "Not like it matters so I\'m not even sure why I wrote that, I just couldn\'t keep it to myself anymore."
    print "You told me that you love me, but you\'re no longer in love with me. I\'ll stop asking you about when you fell out of love, but if you ever figure it out, %s." % (random.choice(share))
    print "After everything we’ve been through, though, I think %s." % (random.choice(outcome))
    print "It took a while for me to reply to your letter, I know. But I hope you understand."
    print "I\'ve had to process a lot of things and now I can say that %s." % (random.choice(decision))
    print "That would be the best for the both of us, and I hope you agree."
    sleep (60)
