


import urllib.request
from urllib.error import HTTPError, URLError
import json




# first the app will run and a massege saying "give me your user name" should appear.
# the app then should use this username to access the github profile of the user.
# if the user name is valid it contiues, if not it shoulf raise an error for the user.
# once the app is in the profile it should look for recent activities and bring them back.
# the results should be printed and then close the connection and call it a day.
#
#built-in modules
# type()
# urllib
# JSON
# for
# print()
# try and except 

input_massage = "Write your user name on GitHub:\n"
gitHub_username = input(input_massage)
data = []

once = 0 #just to stop the app after one succsessfull use

try:
    url = f"https://api.github.com/users/{gitHub_username}/events"

    git_response = urllib.request.urlopen(url)
    decoded_data = git_response.read().decode()

    data = json.loads(decoded_data)

    if data == []:
        print("No recent activity found.")
    else:
        print(f"\nRecent activity for {gitHub_username}:")
        print(len(data), "activities")
    # print(json.dumps(data[0], indent=2))
#index the list elemnt, then index the dictionary keies and their value   
    for event in data:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        date_time = event["created_at"]

        repo_name_len = len(repo_name)
        date_time_len = len(date_time)

        formater = ((repo_name_len + date_time_len + 15) // 4)

        if event_type == "WatchEvent":
            print("^^  " * formater, f"\nStarred {repo_name} | {date_time}")
        elif event_type == "PushEvent":
            print(f"^^  " * formater, f"\nPushed commits to {repo_name} | {date_time}")
        else:
            print("^^  " * formater, f"\nDid {event_type} on {repo_name} | {date_time}")

    once =+ 1 #just to stop the app after one succsessfull use

except HTTPError as error:
    if error.code == 404:
         print("Invalid username.")
    elif error.code == 500:
        print("GitHub server error.")
    else:
        print(f"HTTP Error {error.code}")

except URLError:
    print("Could not connect to GitHub. Please check your internet connection.")

except once != 0: #just to stop the app after one succsessfull use
    pass