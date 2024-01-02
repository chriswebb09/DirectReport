#!/usr/bin/env python3

import json
import re
import requests

from DirectReport.datadependencies import appsecrets, prompts


class GoogleAIClient:
    def get_data_from(self, prompt):
        response = self.query(prompt)
        response_data = response["candidates"][0]["output"].replace("```json", " ")
        response_data = response_data.replace("```", " ")
        response_data = response_data.replace("chriswebb09 update ui for reports 2023-12-24T11:41:37Z", " ")
        return response_data

    def query(self, prompt):
        API_URL = f"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={appsecrets.GOOGLE_AI_TOKEN}"
        headers = {"Content-Type": "application/json"}
        prompt_data = prompts.GENERATE_SUMMARY_PROMPT_PREIX + " " + prompt
        data = {"prompt": {"text": f"{prompt_data}"}}
        response = requests.post(API_URL, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("success")
            print(response.text)
            data = json.loads(response.text)
        else:
            print("error")
            print(response.status_code)
            data = {}
        return data

