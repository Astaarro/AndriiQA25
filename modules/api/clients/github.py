import requests

class Github:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories', params={"q": name})
        body = r.json()

        return body
    

#INDIVIDUAL TESTS

    def emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return body
    
    def emojis_response(self):
        response = requests.get("https://api.github.com/emojis")
      
        return response
    

    def commit(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        body = r.json()

        return body
    
    def commit_responce(self, owner, repo):
        response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    
        return response
    