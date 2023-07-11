import os
import sys
from fast_mail_parser import parse_email, ParseError
import re
import pandas as pd
emlpath = sys.argv[1]
csvpath = sys.argv[2]

emailtext = []
for root, dirs, files in os.walk(emlpath): #emlファイルが入ってるフォルダー
     for file in files:
         if not file.startswith("."):
            with open(os.path.join(root, file), "r") as auto:
                message_payload = auto.read()
                try:
                    email = parse_email(message_payload)
                except ParseError as e:
                    print("Failed to parse email: ", e)
                    sys.exit(1)
            print(email.text_plain)
            emailtext.append(email.text_plain)


exp = []
for text in emailtext:
    code = re.findall(r"B2360\d{4}", str(text))
    exp.append(code)
flat = [x for row in exp for x in row]
df = pd.DataFrame(flat)
df.to_csv(csvpath) #csvファイルの出力先
print(df.value_counts())