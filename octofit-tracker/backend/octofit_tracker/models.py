from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Example collections
users = db['users']
teams = db['teams']
activity = db['activity']
leaderboard = db['leaderboard']
workouts = db['workouts']