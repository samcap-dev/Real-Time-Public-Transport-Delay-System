import requests
import json
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict, MessageToJson

url = "https://cdn.mbta.com/realtime/TripUpdates.pb"

response = requests.get(url)
feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)

for entity in feed.entity:
    print(entity)

# Convert feed to a dict before dumping to JSON
feed_dict = MessageToDict(feed)

with open("data/sample_data.json", "w") as f:
    json.dump(feed_dict, f, indent=2)