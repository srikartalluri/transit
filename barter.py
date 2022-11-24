from google.transit import gtfs_realtime_pb2
import urllib.request as ur

feed = gtfs_realtime_pb2.FeedMessage()
response = ur.urlopen('http://api.bart.gov/gtfsrt/tripupdate.aspx')
feed.ParseFromString(response.read())



for entity in feed.entity:
  print(entity)
  #if entity.HasField('trip_update'):
    #print(entity.trip_update)