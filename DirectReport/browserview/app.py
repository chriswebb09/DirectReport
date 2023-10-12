#!/usr/bin/env python3

# Flask

from flask import Flask, render_template, request, redirect, jsonify, json

# OpenAI 

import openai
import secrets
import prompts
#
# from transformers import AutoModelForCausalLM
# from transformers import pipeline
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
#

# def test():
#     access_token = "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"
#
#     # torch.set_default_device('cuda')
#     model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")
#     tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")
#     inputs = tokenizer('''```python
#     def print_prime(n):
#        """
#        Print all primes between 1 and n
#        """''', return_tensors="pt", return_attention_mask=False)
#
#     outputs = model.generate(**inputs, max_length=200)
#     text = tokenizer.batch_decode(outputs)[0]
#     print(text)


openai.api_key = secrets.SECRET_KEY

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """
    Renders the homepage of the web application.
    :return: Rendered HTML template for the homepage.
    """
    #test()
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors (page not found).

    :param e: The error object.
    :return: Rendered HTML template for the 404 error page.
    """
    return render_template('404.html', error=e), 404

@app.route("/account", methods=['GET', 'POST'])
def account():
    return render_template('account.html', title='Account')

@app.route("/teamreport", methods=['GET', 'POST'])
def team_report():
    if request.method == "POST":
        print("POST")
    return render_template('teamreport.html', title='Team Report', data=[])

@app.route("/report", methods=['GET', 'POST'])
def report():
    prompt = ""
    if request.method == "POST":
        prompt = request.get_json()["prompt"]
    #     print(prompt)
    # elements = {
    #     "team": [
    #         {
    #             "name": "AdrianPrantl",
    #             "accomplishments": "AdrianmadesignificantcontributionstotheDebugInfoandSILGen,includingaddingsupportfordebuginfoforcoroutineallocas,inlinedandspecializedgenericvariables.Healsoworkedonthemanglingtestcase,fixedsourcelocationsofvariableassignmentsandfunctioncalls,andaddedbuild-scriptsupportforSwiftLLDBbackwards-compatibilitytests.",
    #             "commits": "67"
    #         },
    #         {
    #             "name": "AhmadAlhashemi",
    #             "accomplishments": "AhmadworkedontheParser,detectingnonbreakingspaceU+00A0andprovidingafix.Healsomademinorstyleeditsandaddedmorenon-breakingspacetestcases.",
    #             "commits": "5"
    #         },
    #         {
    #             "name": "AkshayShrimali",
    #             "accomplishments": "AkshayupdatedtheREADME.mdfile.",
    #             "commits": "1"
    #         },
    #         {
    #             "name": "AlanZeino",
    #             "accomplishments": "AlanfixedatypointhecodeexampleinlibSyntaxREADME.",
    #             "commits": "1"
    #         },
    #         {
    #             "name": "Albin\"albinek\"Sadowski",
    #             "accomplishments": "AlbinfixedsyntaxhighlightinginCHANGELOG.",
    #             "commits": "1"
    #         },
    #         {
    #             "name": "Alejandro",
    #             "accomplishments": "Alejandroremovedawarning,madesomedocumentationfixes,fixedBinaryFloatingPoint.random(in:)openrangereturningupperBound,andfixedaminorcodetypoinSILPro..Man..md.",
    #             "commits": "3"
    #         },
    #         {
    #             "name": "AlexBlewitt",
    #             "accomplishments": "Alexworkedonseveralfixesincludingcompareforlhsandrhs,using||insteadof&&forkindcomparison,removingduplicateconditionalcheckandduplicateifstatement.",
    #             "commits": "5"
    #         }
    #     ],
    #     "report": {
    #         "summary": "Theteammadesignificantprogressthisweekwithatotalof83commits.ThemainfocuswasonDebugInfoandSILGenenhancements,Parserimprovements,andvariousfixes.",
    #         "highlights": [
    #             {
    #                 "title": "DebugInfoandSILGenEnhancements",
    #                 "description": "AdrianPrantlmadesignificantcontributionstotheDebugInfoandSILGen,includingaddingsupportfordebuginfoforcoroutineallocas,inlinedandspecializedgenericvariables."
    #             },
    #             {
    #                 "title": "ParserImprovements",
    #                 "description": "AhmadAlhashemiworkedontheParser,detectingnonbreakingspaceU+00A0andprovidingafix."
    #             },
    #             {
    #                 "title": "VariousFixes",
    #                 "description": "Theteamworkedonseveralfixesincludingcompareforlhsandrhs,using||insteadof&&forkindcomparison,removingduplicateconditionalcheckandduplicateifstatement."
    #             }
    #         ],
    #         "conclusion": "Theteamdemonstratedgoodprogressthisweek,withafocusonenhancingDebugInfoandSILGen,improvingtheParser,andimplementingvariousfixes.Theteamshouldcontinuetofocusontheseareasinthecomingweek."
    #     }
    # }

    report = get_team_summarys_from_git_shortlog(prompt)
    elements = report.choices[0].message.content
    elements = elements.replace("'", '"')
    elements = elements.replace('"albinek"', '')
    json_object = json.loads(elements)
    return elements, 201

@app.route("/generate_email", methods=['POST'])
def generate_email():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    print(prompt)
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201

def get_team_summarys_from_git_shortlog(data):
    prompt =  prompts.GENERATE_SUMMARY_PROMPT_PREIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.1,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response

def generate_email(data):
    prompt =  prompts.GENERATE_EMAIL_PROMPT_PREFIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.1,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    print(response)
    return response


if __name__ == "__main__":
    app.run()
