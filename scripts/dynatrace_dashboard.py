import requests

# Construct the API endpoint URL
dynatrace_instance = "wmj70051.live.dynatrace.com"
url = f"https://{dynatrace_instance}/api/config/v1/dashboards"
access_token = "<key_here>"
# Set headers including the authentication
headers = {
    "Authorization": f"Api-Token {access_token}",
    "accept": "application/json; charset=utf-8"
}

def get_dashboards():

    # Send GET request to fetch pull request details
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dashboards = response.json()
        print(dashboards['dashboards'])

    return response.json()
    ## print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    get_dashboards()
