import openai
from DirectReport.datadependencies import appsecrets, prompts

openai.api_key = appsecrets.SECRET_KEY
def generate_email(data):
    prompt = prompts.GENERATE_EMAIL_PROMPT_PREFIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.1,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response

def get_team_summarys_from_git_shortlog(data):
    prompt = prompts.GENERATE_SUMMARY_PROMPT_PREIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response
