class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_content = collections.defaultdict(list)
        self.user_follow = collections.defaultdict(set)
        self.tweet_consequence = {}
        self.count  = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.count += 1
        self.tweet_consequence[tweetId] = self.count
        self.tweet_content[userId].append(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        self.user_follow[userId].add(userId)
        arr = []

        for f in self.user_follow[userId]:
            arr += self.tweet_content[f]
        
        return sorted(arr, key = lambda x:self.tweet_consequence[x], reverse = True)[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_follow[followerId].add(followerId)
        self.user_follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.user_follow and followeeId in self.user_follow[followerId]:
            self.user_follow[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
