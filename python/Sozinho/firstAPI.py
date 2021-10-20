import requests

#username = input("What the user you are searching? ")


def getUserPublicRepos(username='Japaneixxx'):
    link = f'https://api.github.com/users/{username}'
    r = requests.get(link)
#    print(r.status_code)
#    print(r.json()['public_repos'])
    return r.json()['public_repos']


def getUserFollowers(username='Japaneixxx'):
    link = f'https://api.github.com/users/{username}'
    r = requests.get(link)
#    print(r.status_code)
#    print(r.json()['public_repos'])
    return r.json()['followers']


def printUserInfos(user='Japaneixxx'):
    print(getUserPublicRepos(user))
    print(getUserFollowers(user))


printUserInfos(input('What is the user you are searching? '))
