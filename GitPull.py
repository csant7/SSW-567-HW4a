'''
Created on Sep 18, 2019

@author: Connor Santiago
'''
import json
import requests

def gitHubAPI(gitID):
    webURL = "http://api.github.com/users/" + gitID + "/repos" 
    repository = requests.get(webURL)
    userRepository = repository.json()
   
    repositoryList = []
    
    for repos in userRepository: 
        commitURL = "https://api.github.com/repos/" + gitID + "/" + repos["name"] + "/commits"
        commits = requests.get(commitURL)
        commits = json.loads(commits.content.decode('utf-8'))
        comNum = len(commits)
      
        print("User ID: " + gitID + "Repo: " + repos["name"] + " Number of Commits: " + str(comNum))
        repositoryList.append((str(repos["name"]), comNum))
  
    return repositoryList

if __name__ == "__main__":
    gitHubAPI("csant7")

