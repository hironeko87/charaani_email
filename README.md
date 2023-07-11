# charaani_email
A Python script to decode e-mails sent from Chara-ani.com for quick reference of total slots won for Not equal me offline &amp; online fan meets

## 使い方
用意していただくもの

 - 当選されたemlファイルの入ったフォルダー（MacOSにて標準アプリ”メール”もしくはWindows/Linuxのサードパーティーアプリ”Outlook”などでも出力可能）
   タイトルは「当選のお知らせ」で検索してください。
 - Python環境
   - fast_mail_parser、　以下で事前にインストールしてください
     ```
     pip install fast-mail-parser
     ```

##　原理

キャラアニはイベントの日付と部数を「商品コード」（Bと8桁の数字）で管理されています。　すべての応募が同じ枚数で応募していたら、商品コードが当選メールでの出現回数を集計すると当選された部の合計がわかります。

リクエスト次第で異なる枚数で応募された場合の集計機能も検討していきます。

## Troubleshooting 
推しメンの商品コードがB2360から始まって下4桁だけ異なるので
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


2023-07-12 Ver0.1
