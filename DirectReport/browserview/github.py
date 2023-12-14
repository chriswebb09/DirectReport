#!/usr/bin/env python3

import re
import requests
import json
from DirectReport.datadependencies import appsecrets, prompts


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

    # def get_pull_request_comments_count(repo_owner, repo_name, pull_request_number):
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

    def get_pull_requests_count(self, repo_owner, repo_name):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.
          pull_request_number: The number of the pull request.

        Returns:
          The number of comments on the pull request.
        """

        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return len(response.json())

    def get_user_repos(self, repo_owner):
        url = f"https://api.github.com/users/{repo_owner}/repos?sort=updated&order=desc"
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_repo_issues(self, repo_owner, repo_name):
        headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

class HuggingFaceClient:

    def query(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

class GoogleAIClient:


    def query(self, prompt):
        print(prompts.GENERATE_SUMMARY_PROMPT_PREIX)
        API_URL = f"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={appsecrets.GOOGLE_AI_TOKEN}"
        headers = {"Content-Type": "application/json"}
        prompt_data = prompts.GENERATE_SUMMARY_PROMPT_PREIX + prompt
        data = {"prompt": { "text": f"{prompt_data}"}}
        response = requests.post(API_URL, data=json.dumps(data), headers=headers)
        data = json.loads(response.text)
        return data

    def get_data_from(self, prompt):
        response = self.query(prompt)
        response_data = response["candidates"][0]["output"]
        return response_data

