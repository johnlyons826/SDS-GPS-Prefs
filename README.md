# SDS-GPS-Prefs
Contains code dealing with ranking rooms by user preference comparison and mean distance of a group

# GPSOperations
Stores code for comparing groups of GPS lat/long readings with an end point, to produce an average distance.

# PrefWeights
Deals with creating a weight value for a room given its contents and that of a user.

# TO DO:
- Primary and secondary priorities for users.
  - e.g. group leader has greater weight on some settings etc.
- Integrate distance weighting onto the end of preference weighting.
  - use exponential function to punish further distances?
- Experiment on actual user data (gained from James and Sam's GPS app parser).
- Implement the preference weight bumps after a successful booking.
  - May need to mock up said "successful booking".
- Check Python's rounding/floating points to improve GPS reading accuracy.
