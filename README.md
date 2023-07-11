# charaani_email
A Python script to quickly parse &amp; decode e-mails sent from Chara-ani.com for quick reference of total slots won for Not equal me offline &amp; online fan meets
![イメージ](https://github.com/hironeko87/charaani_email/blob/main/SCR-20230712-r3-2.png)

## 使い方
用意していただくもの

 - 当選されたemlファイル
    - MacOS標準アプリ”メール”もしくはWindows/Linuxのサードパーティーアプリ”Outlook”などでも出力可能
    - タイトルは「当選のお知らせ」で検索してください
    - 該当するメールを全数選択して、空のフォルダーにドロップしてください。
 - Python環境
   - fast_mail_parser　を以下で事前にインストールしてください
     ```
     pip install fast-mail-parser
     ```
**入力するコマンド**
```
python win3.py [emlファイルのフォルダー/]　[csvファイルの出力先.csv]
```

##  原理

キャラアニ・チャンスはイベントの日付と部数を「商品コード」（Bと8桁の数字）で管理されています。
すべての応募が同じ枚数だと、商品コードが当選メールでの出現回数を集計することで当選された部と部の内訳がわかります。

リクエスト次第で異なる枚数で応募された場合の集計機能も検討しています。

## Troubleshooting 
推しメンの商品コードがB2360からはじまる任意の4桁のケースを想定して書いたので

```
win3.py
```
の
26行目
```
    code = re.findall(r"B2360\d{4}", str(text))
```
B2360のところ各自の用途に合わせて調整してください。

If you have any questions, [@hironeko87](https://twitter.com/hironeko87)


2023-07-12 Ver0.1.1
