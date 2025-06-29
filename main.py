from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection
app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host="redis-19553.c301.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=19553,
    decode_responses=True,
    password="WEHppng2LbwDPCEolrujZf8AHehVg2W8",
)
