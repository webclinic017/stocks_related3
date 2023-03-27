import pyetrade

##consumer_key = "5b4f5c99e7bbcb6e4f06f2f8fa703d5"
##consumer_secret = "76b2f46f79e1b21e4a2ab88ee071e7d2e7587a5ad646d0a5332cc083360cc445"


consumer_key = "1974d0d9c9a1b6a303b5802f3dcba880,"
consumer_secret = "e62975961e15375b3abbbeb9946835b0b41e888bcb51fd9d9903f714d2374eac"



oauth = pyetrade.ETradeOAuth(consumer_key, consumer_secret)
print(oauth.get_request_token())  # Use the printed URL

verifier_code = input("Enter verification code: ")
tokens = oauth.get_access_token(verifier_code)
print(tokens)


