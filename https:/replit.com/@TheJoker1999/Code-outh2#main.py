import requests

API_ENDPOINT = "https:///discord.com/api/v8"
CLIENT_ID = "1042923443764604958"
CLIENT_SECRET = "oREVqvmgF7hUsbPkXD0ls35LGwhlebQm"
REDIRECT_URI = "https://google.com"

def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()

def add_to_guild(access_token, userID):
        url = f"{API_ENDPOINT}/guilds/1042928328614609016/members/1035094806524858378"

        botToken = "MTA0MjkyMzQ0Mzc2NDYwNDk1OA.Gp5CGD.2UzUYW4WYJIeg5xm6R4bbjikBqq2XYQm9ByGBQ"
        data = {
        "access_token" : access_token,
    }
        headers = {
        "Authorization" : f"Bot {botToken}",
        'Content-Type': 'application/json'

    }
        response = requests.put(url=url, headers=headers, json=data)
        print(response.text)

code = exchange_code("peSnNkhQnRhuub7l7lkFL5I7GjTa2k")["access_token"]
add_to_guild(code, "1035094806524858378")
