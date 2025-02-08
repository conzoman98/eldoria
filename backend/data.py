import requests
import os
import json

# Request Methods

def download_lorefrog_data():
    url = os.environ['LOREFROG_URL']

    payload = {}
    headers = {
    'X-Lfjwt': os.environ['LOREFROG_JWT'],
    'X-Username': os.environ['LOREFROG_USERNAME']
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def get_campaign_data(slug):
    url = os.environ['LOREFROG_CAMPAIGN_URL']
    url = url.replace('{campaign_slug}', slug)

    payload = {}
    headers = {
    'X-Lfjwt': os.environ['LOREFROG_JWT'],
    'X-Username': os.environ['LOREFROG_USERNAME']
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)


def get_universe_records():
    data = download_lorefrog_data()
    return data['result']['data']['json']['data']['records']


# Filters

def pull_and_filter(filter):
    records = get_universe_records()
    return [record for record in records if record['collection'] == filter]


def filter_down(lst, filter):
    has_name = lambda entry, name: entry['title'] == name
    has_nickname = lambda entry, nickname: nickname in entry['nicknames']
    has_id = lambda entry, id: entry['id'] == id
    return [entry for entry in lst if has_name(entry, filter) or has_nickname(entry, filter) or has_id(entry, filter)]


# Campaign Information

def get_list_of_campaigns():
    lorefrog_data = download_lorefrog_data()
    campaigns = lorefrog_data['result']['data']['json']['data']['campaigns']
    return campaigns

def get_campaign(slug):
    campaign_data = get_campaign_data(slug)
    return campaign_data['result']['data']['json']['data']['campaign']

# Session Information

def get_campaign_sessions(slug):
    campaign_data = get_campaign_data(slug)
    return campaign_data['result']['data']['json']['data']['sessions']


# Player Character Information

def get_all_player_characters():
    return pull_and_filter('players')


def get_player_character(name):
    characters = get_all_player_characters()
    named_character = filter_down(characters, name)
    if len(named_character) > 0:
        return named_character[0]
    return f"No character found named {name}"


# NPC Information

def get_all_npcs():
    return pull_and_filter('npcs')


def get_npc(name):
    npcs = get_all_npcs()
    named_entry = filter_down(npcs, name)
    if len(named_entry) > 0:
        return named_entry[0]
    return f"No character found named {name}"


# Location Information

def get_all_locations():
    return pull_and_filter('locations')


def get_location(name):
    locations = get_all_locations()
    named_entry = filter_down(locations, name)
    if len(named_entry) > 0:
        return named_entry[0]
    return f"No location found named {name}"


# Creation Information

def get_all_creations():
    return pull_and_filter('creations')


def get_creation(name):
    creations = get_all_creations()
    named_entry = filter_down(creations, name)
    if len(named_entry) > 0:
        return named_entry[0]
    return f"No creation found named {name}"


# History Information

def get_all_history():
    return pull_and_filter('history')


def get_history(name):
    histories = get_all_history()
    named_entry = filter_down(histories, name)
    if len(named_entry) > 0:
        return named_entry[0]
    return f"No history found named {name}"
