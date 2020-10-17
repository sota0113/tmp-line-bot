# TMP line bot
## Description
内輪向けの筋トレ管理LINEボット  
## Architecture
メインロジックの[lambda_function.py](./lambda_function.py)はAWS Lambdaで動作。  
現在DB不在。なるべくお金がかからないサービスを選定中。  
![image](./image/goApiServer.png)

https://github.com/sota0113/tmp-line-bot/blob/main/image/tmp-architecture.png

## Deployment
AWS Lambdaのpython3.xのデフォルト環境では不足するライブラリがあるため、必要なファイル一式をzipでアップロードする必要があります。   
今回不足したreqstsライブラリは既に本repoに用意済みですが念の為以下に手順を記します。  
```
mkdir -p tmp-repo/package
cd tmp-repo/package
pip3 install requests --target .
zip -r9 ../function.zip .
```

以下コマンドで`function.zip`を作成し、Lambdaに展開します。  
```
zip -g function.zip lambda_function.py
```

## 今後
・DBの選定。  
・回数カウントロジック。  
・回数モニタリングと未達者へのアラート発報。  
・自然言語処理。正規表現では限界。 
