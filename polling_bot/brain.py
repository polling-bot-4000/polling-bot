import requests


class SlackClient:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def post_message(self, message):
        r = requests.post(self.webhook_url, json={"text": message})

    def post_messages(self, messages):
        for message in messages:
            self.post_message(message)


class GitHubClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def raise_issue(self, owner, repo, title, body):
        url = 'https://api.github.com/repos/%s/%s/issues' % (owner, repo)
        r = requests.post(url,
            json={'title': title, 'body': body},
            headers={'Authorization': 'token %s' % (self.api_key)}
        )
