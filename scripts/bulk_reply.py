# first merge the two source files to pair ticket # with macro references
# post a comment on a ticket
# given the ticket number and a reference to which macro to use
# some kind of output file to record any potential edge cases/failures
from base64 import b64encode
import pandas as pd
import configparser
import requests
import json
import time
import sys

config = configparser.RawConfigParser()
config.read('./src/auth.ini')
DOMAIN = config['zendesk']['Domain'].strip('"')
AUTH = config['zendesk']['Credentials'].strip('"')

def main():
    formatter()

def formatter():
    macro = macro_data()
    users = pd.read_csv('./src/users.csv', header=None)
    # print(users)
    for row in users:
        while row:        
            ticket_num = []
            while len(ticket_num) <= 100:        
                ticket_num.append(users[0])
                row = row + 1
            print(ticket_num)
            # exit()
            post_comment(ticket_num, macro)
            return ticket_num
    
    print("No more ticket IDs found.")
    time.sleep(1)
    print("Uploading 637 Petabytes of illegal material to your computer in:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Lmao joking. Bye Bye!")

def post_comment(ticket_num, macro):
        ticket_num = formatter()
        url = 'https://{}.zendesk.com/api/v2/tickets/update_many.json?ids={}'.format(DOMAIN, ticket_num)
        print("URL, ", url)
        header = {"Authorization": "Basic {}".format(str(b64encode(AUTH.encode('utf-8')))[2:-1]), 'Content-type': 'application/json'}
        print("HEADER, ", header)
        dat = macro_data(macro)
        print("DATA, ", dat)
        try:
            result = requests.put(url, data=json.dumps(dat), headers=header)
            result = json.loads(result.text)
            jobstatus_url = result["job_status"]["url"]
            print("Follow this link for the job status: " + jobstatus_url)
            jobstatus = requests.get(jobstatus_url, headers=header)
            jobstatus = json.loads(jobstatus.text)
            while jobstatus["job_status"]["status"] != "completed":
                jobstatus = requests.get(jobstatus_url, headers=header)
                jobstatus = json.loads(jobstatus.text)
                print("Progress: " + jobstatus["progress"])
                print("Refreshing: 10 second wait time...")
                time.sleep(10)
                return result
            else:
                print("Done! Checking for more tickets to update.")
        except Exception as e:
            print('Error posting comments', str(e))
            exit()



def macro_data(): 
    scenario = ("Hi there,\n"
                "Thanks for reaching out and we apologize for the delayed response!\n\n"
                "Here's a new link for the 60-day free trial:\n\n"
                "https://www.crunchyroll.com/welcome/nextlevel?coupon_code="+str("code")+"&campaign=funimation\n\n"
                "If for any reason you should still need assistance with anything please don't hesitate to reach out to us. Thanks and have a great day!")

    formatted = {"ticket": {"assignee": {"id" :399987185412, "email": "daniel.galca@ellation.com"}, "comment": { "body": "{}".format(scenario), "public": True}}} 
    return formatted

if __name__ =="__main__":
    # args = sys.argv
    main()