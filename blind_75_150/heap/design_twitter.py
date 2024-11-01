from typing import List, Dict, Set
import heapq


class User:
    def __init__(self) -> None:
        self.fan_ids: Set[int] = set()
        self.idol_ids: Set[int] = set()
        self.feed = []
        self.self_posts = []


class Twitter:

    def __init__(self):
        self.id_to_user: Dict[int, User] = dict()
        self.time = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.time += 1
        # * If this is the FIRST TIME we see this id
        if user_id not in self.id_to_user:
            user = User()
            self.id_to_user[user_id] = user
            # * He does NOT have any idols
        # * We will have to post this thing into
        # * his OWN and his FANS account

        # * HIS OWN account
        user = self.id_to_user[user_id]
        heapq.heappush(user.feed, (-self.time, user_id, tweet_id))
        heapq.heappush(user.self_posts, (-self.time, tweet_id))
        # * HIS FANS
        for fan_id in user.fan_ids:
            fan = self.id_to_user[fan_id]
            heapq.heappush(fan.feed, (-self.time, user_id, tweet_id))

    def getNewsFeed(self, user_id: int) -> List[int]:
        count = 0
        if user_id not in self.id_to_user:
            self.id_to_user[user_id] = User()
            return []
        user = self.id_to_user[user_id]
        res = []
        while count < 10 and user.feed:
            neg_time, user_id_from_tweet, tweet_id = heapq.heappop(user.feed)
            if (
                user_id_from_tweet == user_id or user_id_from_tweet in user.idol_ids
            ) and (neg_time, user_id_from_tweet, tweet_id) not in res:
                res.append((neg_time, user_id_from_tweet, tweet_id))
                count += 1
        for group in res:
            heapq.heappush(user.feed, group)
        return [ele[2] for ele in res]

    def follow(self, fan_id: int, idol_id: int) -> None:
        if fan_id not in self.id_to_user:
            self.id_to_user[fan_id] = User()
        if idol_id not in self.id_to_user:
            self.id_to_user[idol_id] = User()
        fan = self.id_to_user[fan_id]
        idol = self.id_to_user[idol_id]
        fan.idol_ids.add(idol_id)
        idol.fan_ids.add(fan_id)
        # * We will need to dump all the idol's self_posts into the user's feed
        for neg_time, tweet_id in idol.self_posts:
            heapq.heappush(fan.feed, (neg_time, idol_id, tweet_id))

    def unfollow(self, fan_id: int, idol_id: int) -> None:
        if fan_id not in self.id_to_user:
            self.id_to_user[fan_id] = User()
        if idol_id not in self.id_to_user:
            self.id_to_user[idol_id] = User()
        fan = self.id_to_user[fan_id]
        idol = self.id_to_user[idol_id]
        if idol_id in fan.idol_ids:
            fan.idol_ids.remove(idol_id)
        if fan_id in idol.fan_ids:
            idol.fan_ids.remove(fan_id)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

