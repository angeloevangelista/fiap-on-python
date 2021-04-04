from github import Github

API_KEY = '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'

githubInstance = Github(
  base_url = "https://api.github.com",
  login_or_token = API_KEY
)

for repo in githubInstance.get_user('angeloevangelista').get_repos():
  print(repo.name)
