
#app7.py
from openai import OpenAI
import requests
import pandas as pd
import time
import os
import json

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')

# Your assistant ID
assistant_id = 'asst_GQBiZDRsZTC1zMSQ9TKNjLRH'

# Open-API keys for each sport, excluding NFL
api_keys = {
    "nba": "ehjp5frfgkkbgjz392gqczjq",
    "mlb": "gv8j89h95brmckzfbshfgkxc",
    "nhl": "4jtt2zm2rjgg42petfnwkh9r",
    "ncaamb": "x6skf83zw7hzhkepqy4urvvr",
}

# API versions for each sport, excluding NFL
api_versions = {
    "nba": "v8/en/seasons/2023/REG",
    "mlb": "v7/en/seasons/2023/REG",
    "nhl": "v7/en/seasons/2023/REG",
    "ncaamb": "v8/en/polls/AP/2023",
}
api_versions2 = {
    "nba": "v8",
    "mlb": "v7",
    "nhl": "v7",
    "ncaamb": "v8/en/polls/AP/2023",
}

# Generalized function to fetch and save rankings
def fetch_rankings(sport, api_key):
    version = api_versions[sport]
    url = f"http://api.sportradar.us/{sport}/trial/{version}/rankings.json?api_key={api_key}"
    standings_file = f"{sport}_Standings.json"  # Changed to .json
    # Check if file exists and delete it
    if os.path.exists(standings_file):
        os.remove(standings_file)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Ensure data is in JSON format
        with open(standings_file, "w") as file:
            json.dump(data, file, indent=4)  # Write JSON data to file
    
    # Handling for NCAAMB data
    if sport == 'ncaamb':
        data = response.json()
        teams_data = [
            {"ID": team["id"], "Name": team["name"], "Market": team["market"]}
            for team in data.get("rankings", [])
        ]
    
    # Handling for MLB data
    elif sport == 'mlb':
        data = response.json()["league"]["season"]["leagues"]
        teams_data = []
        for league in data:
            for division in league["divisions"]:
                for team in division["teams"]:
                    teams_data.append({
                        "ID": team["id"],
                        "Name": team["name"],
                        "Market": team["market"]
                    })
    
    # Default handling for other sports
    else:
        data = response.json()
        teams_data = [
            {"ID": team.get("id"), "Name": team.get("name"), "Market": team.get("market")}
            for conference in data.get("conferences", []) 
            for division in conference.get("divisions", []) 
            for team in division.get("teams", [])
        ]
    
    team_ids_file = f"{sport}_Team_IDs.csv"
    # Check if file exists and delete it
    if os.path.exists(team_ids_file):
        os.remove(team_ids_file)
    pd.DataFrame(teams_data).to_csv(team_ids_file, index=False)

# Generalized function to fetch team statistics

def fetch_team_stats(sport, api_key):
    version = api_versions[sport]
    teams_df = pd.read_csv(f"{sport}_Team_IDs.csv")
    all_team_stats = []  # Use a list to hold JSON data for each team's stats
    for team_id in teams_df["ID"]:
        if sport == 'ncaamb':
            url = f"http://api.sportradar.us/ncaamb/trial/v8/en/seasons/2023/REG/teams/{team_id}/statistics.json?api_key={api_key}"
        else:
            url = f"http://api.sportradar.us/{sport}/trial/{version}/teams/{team_id}/statistics.json?api_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            team_stats = response.json()  # Parse the JSON response directly
            all_team_stats.append(team_stats)  # Append the team's stats to the list
        
        # Convert current list of team stats to string to check size
        content_str = json.dumps(all_team_stats)
        if len(content_str.encode('utf-8')) > 2000000:  # Check if content size exceeds 2,000,000 bytes
            file_suffix = "" if not os.path.exists(f"{sport}_season_stats.json") else "1"
            with open(f"{sport}_season_stats{file_suffix}.json", "w") as file:
                file.write(content_str)
            all_team_stats = []  # Reset list for potentially next file
        time.sleep(1)
    
    # After loop, write remaining content to file or second file if split occurred
    if all_team_stats:  # Check if there's any content left to write
        file_suffix = "" if not os.path.exists(f"{sport}_season_stats.json") else "1"
        with open(f"{sport}_season_stats{file_suffix}.json", "w") as file:
            # Since all_team_stats is already a list of JSON objects, dump it directly
            json.dump(all_team_stats, file, indent=4)


# Generalized function to fetch and save injuries data
def fetch_injuries(sport, api_key):
    version = api_versions2[sport]
    url = f"http://api.sportradar.us/{sport}/trial/{version}/en/league/injuries.json?api_key={api_key}"
    injuries_file = f"{sport}_Injuries.json"  # Changed to .json
    # Check if file exists and delete it
    if os.path.exists(injuries_file):
        os.remove(injuries_file)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Ensure data is in JSON format
        with open(injuries_file, "w") as file:
            json.dump(data, file, indent=4)  # Write JSON data to file
    else:
        print(f"Failed to fetch injuries data for {sport}. Status Code: {response.status_code}")

# Call the functions to execute the data fetching and file creation
for sport, api_key in api_keys.items():
    fetch_rankings(sport, api_key)
    fetch_team_stats(sport, api_key)
    fetch_injuries(sport, api_key)

    #delete files from assistant
my_updated_assistant = client.beta.assistants.update(
  assistant_id=assistant_id,
  file_ids=[],
)

print(my_updated_assistant)

# List of file paths you want to match and delete/upload
file_paths = [
    'mlb_Injuries.json', 'mlb_season_stats.json', 'mlb_Standings.json', 'ncaamb_season_stats.json',
    'nba_Injuries.json', 'nba_season_stats.json', 'nba_Standings.json', 'ncaamb_Standings.json',
    'nhl_Injuries.json', 'nhl_season_stats.json', 'nhl_Standings.json', 'mlb_season_stats1.json',
    'nba_season_stats1.json', 'nhl_season_stats1.json', 'ncaamb_season_stats1.json' 
    #'mlb_Team_IDs.csv', 'nba_Team_IDs.csv', 'nhl_Team_IDs.csv', 'ncaamb_Team_IDs.csv'
]

# Fetch the list of files from the client
files_response = client.files.list()

# Assuming files_response.data contains the list of files, each with 'id' and 'filename' attributes
file_id_to_path = {file.filename: file.id for file in files_response.data}

for file_path in file_paths:
    file_id = file_id_to_path.get(file_path)
    if file_id:
        # If the file ID was found in the mapping, proceed to delete the file
        try:
            response = client.files.delete(file_id=file_id)
            print(f"Deleted {file_path}: Response - {response}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    else:
        print(f"File ID not found for {file_path}")

# Loop through each file path in the list for upload
for file_path in file_paths:
    if os.path.exists(file_path):  # Check if the file exists
        # Upload the file and assign the purpose
        with open(file_path, "rb") as file:
            uploaded_file = client.files.create(
                file=file,
                purpose='assistants'
            )
        
        # Extract the file ID from the uploaded file response
        file_id = uploaded_file.id
        
        # Create the file under the assistant using the file ID
        response = client.beta.assistants.files.create(
            assistant_id=assistant_id,
            file_id=file_id
        )
        
        print(f"Uploaded {file_path} and assigned to assistant with response: {response}")
    else:
        print(f"File {file_path} does not exist, skipping upload.")