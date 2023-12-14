#!/usr/bin/env python3

global GENERATE_EMAIL_PROMPT_PREFIX
global GENERATE_SUMMARY_PROMPT_PREIX

GENERATE_EMAIL_PROMPT_PREFIX =  "can you take this data and summarize in professional manner for an email on the team status for my manager?\n" + "Data: "
GENERATE_SUMMARY_PROMPT_PREIX  = "can you provide a short summary of what what was accomplished overall along with the time frame it was accomplished in, please categorize the majors improvements in areas_of__focus and please provide individual breakdown based on the following list of team members and work using the following" + "Format: \n" + "{ \n" + "'team'" + ": [{" + "\n 'name'" + ": '', " + "\n 'accomplishments'" + ": '' " + " ," + "\n 'commits'" + ": '' \n" + "}]," + "\n'report'" + ": {" + "\n 'summary'" + ": " + "\n  'highlights'" + ": [{" + "\n   'title'" + ": '' ," + "\n   'description'" + ": '' "+ "\n }],  \n" + "'areas_of_focus'" + ": [], \n" + " 'conclusion'" + ": ''" + "\n}" + "\n}" + "\n" + "Data:"