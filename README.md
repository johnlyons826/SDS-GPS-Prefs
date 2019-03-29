# SDS-GPS-Prefs
Contains code dealing with ranking rooms by user preference comparison and mean distance of a group

# GPSOperations
Stores code for comparing groups of GPS lat/long readings with an end point, to produce an average distance.

# PrefWeights
Deals with creating a weight value for a room given its contents and that of a user.

# RoomSearch
Contains code for picking a room given a group of user IDs and a time.

# TO DO:
- Primary and secondary priorities for users. (Low priority)
  - e.g. group leader has greater weight on some settings etc.
- use exponential function to punish further distances?
