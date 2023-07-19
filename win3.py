import os
import sys
from fast_mail_parser import parse_email, ParseError
import re
import pandas as pd
emlpath = sys.argv[1]
csvpath = sys.argv[2]
searchmerchid = sys.argv[3]

regex = searchmerchid + "\d{4}"

def read_email(path):
    emailtext = []
    for root, dirs, files in os.walk(path): #emlファイルが入ってるフォルダー
        for file in files:
            if not file.startswith("."):
                with open(os.path.join(root, file), "r") as auto:
                    message_payload = auto.read()
                    try:
                        email = parse_email(message_payload)
                    except ParseError as e:
                        print("Failed to parse email: ", e)
                        sys.exit(1)
                emailtext.append(email.text_plain)
    return emailtext

def search(regexrule,outputpath):
    exp = []
    for text in read_email(emlpath):
        code = re.findall(regexrule, str(text))
        exp.append(code)
    flat = [x for row in exp for x in row]
    df = pd.DataFrame(flat)
    df.to_csv(outputpath) #csvファイルの出力先
    return df.value_counts()
print(read_email(emlpath))
print(search(regex, csvpath))