import json
import os
import re
import requests
import random

auth = os.environ['AUTH']
url = os.environ['ENDPOINT']

def lambda_handler(event, context):
    
    print(event)
    reply_token = event["events"][0]["replyToken"]
    message = event["events"][0]["message"]["text"]

    
    match = bool(re.match(r".*完了.*", message))
    if match == True:
        return_msg = "「完了」の正規表現で拾っています。DDBが無いから記憶できない。すまん。"
        message_to_line(reply_token,return_msg)
        
    #match = bool(re.match(r".*休み.*", message))
    match = bool(re.match(r".*休み.*", message))
    if match == True:
        return_msg = "「休み」の正規表現で拾っています。DBが無いから記憶できない。すまん。"
        message_to_line(reply_token,return_msg)
        
    match = bool(re.match(r".*バド.*", message))
    if match == True:
        items_one = ("了解","はいよ","おっけ","はーい")
        items_two = ("",,"","プロテイン忘れずに")
        items_punc_one = ("","","。","！")
        items_punc_two = ("","","。","！")
        num_one = random.randint(0, 3)
        num_two = random.randint(0, 2)
        num_punc_one = random.randint(0, 2)
        num_punc_two = random.randint(0, 2)
        return_msg = items_one[num_one]+items_punc_one[num_punc_one]+items_two[num_two]+items_punc_two[num_punc_two]
        message_to_line(reply_token,return_msg)

    return {
        'statusCode': 200,
        'body': event
    }

"""
        data = {
            "replyToken": reply_token,
            "messages":[
                {
                    "type":"text",
                    "text":"完了の正規表現で拾っています"
                }
            ]
        }
        _ = requests.post(url,headers=headers, json=data)
"""


"""
    elif message == "お休みです":
        data = {
            "replyToken": reply_token,
            "messages":[
                {
                    "type":"text",
                    "text":"お休み了解です"
                }
            ]
        }
        _ = requests.post(url,headers=headers, json=data)
"""
"""
    elif message == "バドミントンです":
        data = {
            "replyToken": reply_token,
            "messages":[
                {
                    "type":"text",
                    "text":"バド了解です"
                }
            ]
        }
        _ = requests.post(url,headers=headers, json=data)
"""


def message_to_line(reply_token,return_msg):
    headers = {'Authorization': 'Bearer '+auth}
    data = {
        "replyToken": reply_token,
        "messages":[
            {
                "type":"text",
                "text":return_msg
            }
        ]
    }
    _ = requests.post(url,headers=headers, json=data)
