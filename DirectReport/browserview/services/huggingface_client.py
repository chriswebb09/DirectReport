#!/usr/bin/env python3

import json
import re

import requests

from DirectReport.datadependencies import appsecrets, prompts

class HuggingFaceClient:
    def query(self, payload):
        API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
