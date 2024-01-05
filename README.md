# jquants_portfolio
J-Quants APIを使って日本株ポートフォリオを分析するツール

# フォルダ構成

JQUANTS_PORTFOLIO
│  .gitignore
│  docker-compose.yaml
│  Dockerfile
│  README.md
│  requirements.txt
│
├─config
│       user-api.toml
│
└─src
        stock.py

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

- docer imageの立ち上げ
```
docker compose up -d --build
```
- docker containerの起動
```
docker compose exec python3 bash
```

## 実行方法

```
python src/stock.py
```

現状は上場株式総数が表示される。