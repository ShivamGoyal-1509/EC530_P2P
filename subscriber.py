import redis

def subscribe_user(user_id: str):
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    pubsub = r.pubsub()
    channel = f"user:{user_id}"
    pubsub.subscribe(channel)

    print(f"[{user_id}] Listening for messages...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"[{user_id}] Received: {message['data']}")

if __name__ == "__main__":
    user = input("Enter your user ID: ")
    subscribe_user(user)