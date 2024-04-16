import requests
import os
from bs4 import BeautifulSoup
from googletrans import Translator
import urllib.parse
def logo():
    print('''
╔───────────────────────────────────────╗
│ ____  ____       _  __        ___   _ │
│|  _ \|  _ \     / \ \ \      / / \ | |│
│| |_) | |_) |   / _ \ \ \ /\ / /|  \| |│
│|  __/|  _ < _ / ___ \ \ V  V / | |\  |│
│|_| (_)_| \_(_)_/   \_(_)_/\_(_)|_| \_|│
╚───────────────────────────────────────╝
                                                                   
    -CoderSigma
                    P - Proficient
                    R - Resourceful
                    A - Avatar
                    W - Web
                    N - Ninja


    ENTER USER NAME BELOW::
    
    ''')
    
def tiktok(username, url):
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def check_facebook_profile(username):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None
        
def check_instagram_profile(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.find('meta', property='og:type', content='profile'):
            return url
    return None

def check_twitter_profile(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": "jUmGwfI022N3uVNxAtBmoDTQV"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'errors' not in data:
            return url
    return None

def check_google_account(username):
    url = f"https://profiles.google.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_reddit_profile(username):
    url = f"https://www.reddit.com/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_youtube_profile(username):
    url = f"https://www.youtube.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_tumblr_profile(username):
    url = f"https://tumblr.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_snapchat_profile(username):
    url = f"https://www.snapchat.com/add/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_github_profile(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_spotify_profile(username):
    url = f"https://open.spotify.com/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_roblox_profile(username):
    url = f"https://www.roblox.com/users/{username}/profile"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_pornhub_profile(username):
    url = f"https://www.pornhub.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_telegram_profile(username):
    url = f"https://web.telegram.org/k/#@{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_ngl_profile(username):
    url = f"https://ngl.link/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def check_douyin_profile(username):
    translator = Translator()
    translated_username = translator.translate(username, src='en', dest='zh-CN').text
    encoded_username = urllib.parse.quote(translated_username)
    url = f"https://www.douyin.com/user/{encoded_username}"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return None

def total_of_result(username):
    total_results = 0
    found_results = []

    # TikTok
    url = f"https://tiktok.com/@{username}"
    result = tiktok(username, url)
    if result:
        total_results += 1
        found_results.append(result)

    # Facebook
    url = f"https://www.facebook.com/{username}"
    result = check_facebook_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Twitter
    url = f"https://twitter.com/{username}"
    result = check_twitter_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Instagram
    url = f"https://www.instagram.com/{username}/"
    result = check_instagram_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Google Account
    result = check_google_account(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Reddit
    result = check_reddit_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # YouTube
    result = check_youtube_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Tumblr
    result = check_tumblr_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Snapchat
    result = check_snapchat_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # GitHub
    result = check_github_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Spotify
    result = check_spotify_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Roblox
    result = check_roblox_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Pornhub
    result = check_pornhub_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Telegram
    result = check_telegram_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # ngl.link
    result = check_ngl_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    # Douyin
    result = check_douyin_profile(username)
    if result:
        total_results += 1
        found_results.append(result)

    return total_results, found_results

if __name__ == "__main__":
    os.system('clear')
    os.system('\n')
    logo()
    username = input(f"\033[92m[+]Username: \033[0m")

    total_results, found_results = total_of_result(username)
    filename = f"{username}.txt"
    with open(filename, "a") as file: 
        file.write(f"\nResults found for '{username}': {total_results}\n\n")
        for result in found_results:
            file.write(result + "\n")
            print(f"\033[92m[+]FOUND\033[0m \033[96m{result}\033[0m") 
    print(f"\nResults saved to '{filename}'")



