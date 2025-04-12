P2P Messaging System with FastAPI and Redis

This project implements a peer-to-peer messaging system in two phases:
	•	Phase 1: Basic client-server chat using Python sockets.
	•	Phase 2: API-based messaging system using FastAPI and Redis Pub/Sub.

Features
	•	Asynchronous message handling with threads
	•	Real-time communication using Redis Pub/Sub
	•	Minimal dependencies and easy to run locally
	•	Extensible design for future enhancements (encryption, persistence, etc.)

⸻

File Structure

p2p-messaging/
├── main.py           # FastAPI API to send messages via Redis Pub/Sub
├── subscriber.py     # Redis client that listens for user-specific messages
├── server.py         # (Phase 1) Socket-based server
├── client.py         # (Phase 1) Socket-based client
├── run-script.sh     # Shell script to check Redis and start FastAPI
└── README.md         # This file



⸻

Requirements
	•	Python 3.8+
	•	Redis installed and running locally
	•	Recommended packages (install with pip):

pip install fastapi uvicorn redis



⸻

Phase 1: Basic Client-Server Chat

Running the Server

python server.py

Running Clients

In a separate terminal:

python client.py

Repeat in other terminals for more clients. Clients can send and receive messages asynchronously.

⸻

Phase 2: API-Based Messaging System (FastAPI + Redis)

1. Start Redis

If Redis is not running:

brew install redis
brew services start redis

Or manually:

redis-server

Verify it’s running:

redis-cli ping

Should return: PONG

2. Start the FastAPI Server

uvicorn main:app --reload

This starts the API at http://127.0.0.1:8000

3. Run a Subscriber Client

In a new terminal:

python subscriber.py

Enter a user ID (e.g., alice) when prompted.

4. Send a Message

Use curl or Postman to send a message to a user:

curl -X POST http://127.0.0.1:8000/send \
-H "Content-Type: application/json" \
-d '{"sender": "bob", "recipient": "alice", "content": "Hello Alice!"}'

The message will appear in the terminal running subscriber.py for the recipient.

⸻

Shell Script (Optional)

To automate Redis check and start the backend:

./run-script.sh

Make it executable if needed:

chmod +x run-script.sh



⸻
