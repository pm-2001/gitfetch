import requests

# Set your access token here
access_token = "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"

# Set the desired username
username = "pm020202pm"

# Set the API endpoint
url = f"https://api.github.com/users/{username}/events"

# Set the headers
headers = {"Authorization": f"Bearer {access_token}"}

# Send the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the user's recent activity
    events_data = response.json()
    for event in events_data:
        event_type = event["type"]
        created_at = event["created_at"]
        print(f"Event Type: {event_type}")
        print(f"Created At: {created_at}")
        print()
else:
    print(f"Request failed with status code {response.status_code}")
