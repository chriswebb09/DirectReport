#!/usr/bin/env python3

import re
import requests
from DirectReport.datadependencies import appsecrets, prompts
from datetime import datetime, timedelta


class GithubClient:
    # Define a function to parse the git shortlog
    def parse_git_shortlog(self, shortlog):
        """
        Parses a git shortlog and returns a dictionary with the author and their commits.

        Args:
          shortlog: The git shortlog string.

        Returns:
          A dictionary with the author and their commits.
        """
        authors = {}
        for line in shortlog.splitlines():
            match = re.match(r"^(.*?)\s+\((.*?)\):", line)
            if match:
                author, commits = match.groups()
                authors[author] = int(commits)
        return authors

    def get_pull_request_comments(self, repo_owner, repo_name):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.

        Returns:
           comments on pull requests.
        """

        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/comments"
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_pull_requests_count(self, repo_owner, repo_name, token):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.
          pull_request_number: The number of the pull request.

        Returns:
          The number of comments on the pull request.
        """

        thirty_days_ago = datetime.now() - timedelta(days=30)
        since = thirty_days_ago.isoformat()
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            response.raise_for_status()
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_count

    def get_pull_requests_count_sixty_days(self, repo_owner, repo_name, token):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.
          pull_request_number: The number of the pull request.

        Returns:
          The number of comments on the pull request.
        """

        thirty_days_ago = datetime.now() - timedelta(days=60)
        since = thirty_days_ago.isoformat()
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            response.raise_for_status()
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_count

    def get_user_repos(self, repo_owner, token):
        url = f"https://api.github.com/users/{repo_owner}/repos?sort=updated&order=desc"
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_repo_issues(self, repo_owner, repo_name, token):
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_commits_count_in_last_month(self, repo_owner, repo_name, token):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        since = thirty_days_ago.isoformat()
        headers = {"Authorization": f"token {token}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_count

    def get_commits_in_last_month(self, repo_owner, repo_name, token):
        thirty_days_ago = datetime.now() - timedelta(days=30)
        since = thirty_days_ago.isoformat()
        headers = {"Authorization": f"token {token}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        commits_data = []
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            commits_data.extend(commits)
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_data

    def get_commits_count_in_last_sixty_days(self, repo_owner, repo_name, token):
        sixty_days_ago = datetime.now() - timedelta(days=60)
        since = sixty_days_ago.isoformat()
        headers = {"Authorization": f"token {token}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_count

    def get_commits_count_in_last_ninety_days(self, repo_owner, repo_name, token):
        ninety_days_ago = datetime.now() - timedelta(days=90)
        since = ninety_days_ago.isoformat()
        headers = {"Authorization": f"token {token}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
        commits_count = 0
        page = 1
        per_page = 100  # Number of results per page
        while True:
            # Make a request to the GitHub API
            response = requests.get(url, headers=headers, params={'since': since, 'page': page, 'per_page': per_page})
            if response.status_code != 200:
                # Break the loop if the response is not successful
                break
            commits = response.json()
            current_count = len(commits)
            commits_count += current_count
            if current_count < per_page:
                break
            page += 1
        return commits_count
