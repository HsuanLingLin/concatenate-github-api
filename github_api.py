import pandas as pd
import requests
from datetime import datetime


class github_api:
    def __init__(self, username, token):
        self.auth = (username, token)

    def call_github_api(self, per_page):
        df = pd.DataFrame(columns=['repository_ID', 'name', 'URL',
                                   'created_date',  'description', 'number_of_stars'])
        results = requests.get(
            f'https://api.github.com/search/repositories?q=stars%3A%3E100&s=stars&sort=stars&per_page={per_page}', auth=self.auth).json()
        return df, results

    def get_top_100_repos(self, df, results):
        for repo in results['items']:
            top_100_repos = {'repository_ID': repo['id'],
                             'name': repo['name'],
                             'URL': repo['html_url'],
                             'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                             'description': repo['description'],
                             'number_of_stars': repo['stargazers_count']}
            df = df.append(top_100_repos, ignore_index=True)
        print(df)

    def get_top_one_repo(self, df, results):
        repo = results['items'][0]
        top_one_repo = {'repository_ID': repo['id'],
                        'name': repo['name'],
                        'URL': repo['html_url'],
                        'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                        'description': repo['description'],
                        'number_of_stars': repo['stargazers_count']}
        df = df.append(top_one_repo, ignore_index=True)
        print(df)

    def get_specific_repo(self, df, results, id):
        repo = results['items'][id - 1]
        specific_repo = {'repository_ID': repo['id'],
                         'name': repo['name'],
                         'URL': repo['html_url'],
                         'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                         'description': repo['description'],
                         'number_of_stars': repo['stargazers_count']}
        df = df.append(specific_repo, ignore_index=True)
        print(df)
