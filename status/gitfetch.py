import requests

access_token = "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"

def user(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    user_data = response.json()
    return user_data

def repo(username,repo):
    print(username)
    print(repo)
    url = f"https://api.github.com/repos/{username}/{repo}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    user_repo_data = response.json()
    return user_repo_data

def alluserrepo(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    user_data = response.json()
    return user_data

def allrep():
    query = "is:public"  # Filter to public repositories
    sort = "stars"  # Sort by stars (you can choose other sorting options)
    order = "desc"  # Sort in descending order
    base_url = "https://api.github.com"
    endpoint = "/search/repositories"
    headers = {"Authorization": f"Bearer {access_token}"}
    page = 1
    per_page = 10 # The maximum number of results per page
    while page == 1:
        params = {
            "q": query,
            "sort": sort,
            "order": order,
            "page": page,
            "per_page": per_page,
        }
        response = requests.get(base_url + endpoint, headers=headers, params=params)
        if response.status_code == 200:
            repositories_data = response.json()["items"]
            return repositories_data
        else:
            print(f"Request failed with status code {response.status_code}")
            break

    def event(username):
        url = f"https://api.github.com/users/{username}/events"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        event_data = response.json()
        return event_data