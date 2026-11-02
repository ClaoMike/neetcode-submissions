from collections import defaultdict
from heapq import *

class Twitter:
    class User:
        def __init__(self, ID=None):
            self.ID = ID
            self.followers = set()

        def follows(self, userId):
            self.followers.add(userId)
        
        def unfollows(self, userId):
            self.followers.discard(userId)

    def __init__(self):
        self.users = defaultdict(self.User)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUserIfItDoesNotExists(userId)

        self.tweets.append( (tweetId, userId) )

    def getNewsFeed(self, userId: int) -> List[int]:
        self.createUserIfItDoesNotExists(userId)

        user = self.getUser(userId)

        users_that_can_appear_in_feed = [userId]
        users_that_can_appear_in_feed.extend(list(user.followers))
        users_that_can_appear_in_feed = set(users_that_can_appear_in_feed)
        
        most_10_recent = []
        count = 10
        for i in reversed(range(len(self.tweets))):
            tweetId, userId = self.tweets[i]
            if userId in users_that_can_appear_in_feed and count > 0:
                most_10_recent.append(tweetId)
                count -= 1

        return most_10_recent
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUserIfItDoesNotExists(followeeId)
        self.createUserIfItDoesNotExists(followerId)

        user = self.getUser(followerId)
        user.follows(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUserIfItDoesNotExists(followeeId)
        self.createUserIfItDoesNotExists(followerId)

        user = self.getUser(followerId)
        user.unfollows(followeeId)

    def createUserIfItDoesNotExists(self, userId: int) -> None:
        if userId not in self.users.keys():
            new_user = self.User(userId)
            self.users[userId] = new_user
    
    def getUser(self, ID: int) -> self.User:
        self.createUserIfItDoesNotExists(ID)

        return self.users[ID]