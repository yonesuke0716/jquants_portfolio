# jquants_portfolio
J-Quants APIを使って日本株ポートフォリオを分析するツール

詳細は以下の著者のブログ記事を参照ください。

[日本株のポートフォリオを自分で分析できるツールをPythonで作りたい](https://tech-useit-wealth.com/%e3%80%90j-quants-api%e3%80%91%e6%97%a5%e6%9c%ac%e6%a0%aa%e3%81%ae%e3%83%9d%e3%83%bc%e3%83%88%e3%83%95%e3%82%a9%e3%83%aa%e3%82%aa%e3%82%92%e8%87%aa%e5%88%86%e3%81%a7%e5%88%86%e6%9e%90%e3%81%a7)

# フォルダ構成

<pre>
JQUANTS_PORTFOLIO
 |  # 開発環境用
 ├─  .gitignore
 ├─ docker-compose.yaml
 ├─ Dockerfile
 ├─ README.md    
 ├─ requirements.txt
 │
 ├─ config
 │    user-api.toml    # APIキー
 │
 └─ src
      stock.py    # 実行用 
</pre>

git clone時は「config」フォルダは存在しない。

後述の「user-api.tomlの作成」で作成する。

## 準備
### J-Quants APIアカウントの登録

公式HPでアカウントを作成し、「メールアドレス」と「パスワード」を記録する。

https://jpx-jquants.com/

### user-api.tomlの作成

configフォルダ内に「user-api.toml」という名前でファイルを作成する。

作成したファイル内に、以下のように記述する
```
[jquants-api-client]
mailaddress = "your-email"
password = "your-password"
```

"your-email"に「メールアドレス」、"your-password"に「パスワード」をコピペする。

## 開発環境の準備
### 仮想環境の場合

```
pip install -r requirements.txt
```

### Dockerの場合

- docerイメージのビルド(一度ビルドしたら以降は以下の「dockerコンテナの立ち上げ」からでOK)
```
docker compose build stock_portfolio
```
- dockerコンテナの立ち上げ
```
docker compose up -d stock_portfolio
```
- dockerコンテナの起動(コンテナから出る場合はコマンドで「exit」)
```
docker compose exec -it stock_portfolio bash
```
- dockerコンテナの停止
```
docker compose down
```

## 実行方法

```
python src/stock.py
```