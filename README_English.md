# charaani_email
A Python script to quickly parse &amp; decode e-mails sent from Chara-ani.com for quick reference of total slots won for Not equal me offline &amp; online fan meets

With this script, you can subtotal number of talk events won before the payment is due. 

![イメージ](https://github.com/hironeko87/charaani_email/blob/main/SCR-20230712-r3-2.png)

## How to use
Preperation

- eml files that indicate you have won a specific slot
    - You can export eml files from individual emails with MacOS's pre-installed Mail app or any other 3rd party e-mail apps such as "Outlook" on Windows.
    - Search using keyword "当選のお知らせ"
    - Select all that matched the search and drag &amp; drop into an empty folder.
- Python environment
    - Install fast_mail_parser as follows
     ```
     pip install fast-mail-parser
     ```
**Command line usage**

```
python win3.py [folder that has all of the eml files/]　[path to csv file.csv]
```

## How it works
Chara-ani chance manages talk events online or offline with "Merchandise code"(商品コード) that starts with "B" followed by 8 numbers. 

If you applied for talk events with exact same number of CDs, this script counts how many appearances of "Merchandise code" there are in the given e-mails, then subtotals according to "Merchandise code".
Therefore, multiplying appearances of "Merchandise code" with number of CDs you put in, you can get a gist of how many CDs or slots of talk event you won before the payment is due. 

I will also consider putting in functions that recognizes different number of CDs per application. 


## Troubleshooting

Since my oshi's "Merchandise code" all starts with "B2360", you might encounter the problem of script not returning anything. In that case, go to the file win3.py,

on the 26th line
```
    code = re.findall(r"B2360\d{4}", str(text))
```

change "B2360" according to your own application. "\d{4}" means that it will match exactly 4 digits.

If you have any questions, [@hironeko87](https://twitter.com/hironeko87)


2023-07-12 Ver0.1.1
