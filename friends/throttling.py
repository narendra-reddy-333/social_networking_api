from rest_framework.throttling import UserRateThrottle


# for enabling only 3 requests per minute-- currently using memory , cache can be used instead.
class SendFriendRequestRateThrottle(UserRateThrottle):
    rate = '3/minute'
