from dotenv import load_dotenv
from flask import Flask
import data

load_dotenv()
app = Flask(__name__)

@app.route('/api/all', methods=['GET'])
def all_information():
    return data.download_lorefrog_data()

# Campaign Information

@app.route('/api/campaign/list', methods=['GET'])
def get_list_of_campaigns():
    return data.get_list_of_campaigns()

@app.route('/api/campaign/<slug>', methods=['GET'])
def get_campaign(slug):
    return data.get_campaign(slug)

@app.route('/api/campaign/<slug>/sessions/list', methods=['GET'])
def get_campaign_sessions(slug):
    return data.get_campaign_sessions(slug)

# Player Character Information

@app.route('/api/player/list', methods=['GET'])
def all_player_characters():
    return data.get_all_player_characters()

@app.route('/api/player/<name>', methods=['GET'])
def get_player_character(name):
    return data.get_player_character(name)

# NPC Information

@app.route('/api/npc/list', methods=['GET'])
def all_npcs():
    return data.get_all_npcs()

@app.route('/api/npc/<name>', methods=['GET'])
def get_npc(name):
    return data.get_npc(name)

# Location Information

@app.route('/api/location/list', methods=['GET'])
def all_locations():
    return data.get_all_locations()

@app.route('/api/location/<name>', methods=['GET'])
def get_location(name):
    return data.get_location(name)

# Creation Information

@app.route('/api/creation/list', methods=['GET'])
def all_creations():
    return data.get_all_creations()

@app.route('/api/creation/<name>', methods=['GET'])
def get_creation(name):
    return data.get_creation(name)

# History Information

@app.route('/api/history/list', methods=['GET'])
def all_history():
    return data.get_all_history()

@app.route('/api/history/<name>', methods=['GET'])
def get_history(name):
    return data.get_history(name)

if __name__ == "__main__":
    app.run()