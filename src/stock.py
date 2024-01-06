import requests
import json
import tomllib

# =============================================================
# API情報取得
# =============================================================
config_path = "config/user-api.toml"

with open(config_path, mode="rb") as f:
    ret = tomllib.load(f)["jquants-api-client"]
# =============================================================
# API認証情報取得
# =============================================================
# refresh token取得
try:
    req_post = requests.post(
        "https://api.jquants.com/v1/token/auth_user", data=json.dumps(ret)
    )
    REFRESH_TOKEN = req_post.json()["refreshToken"]
except Exception:
    print("RefreshTokenの取得に失敗しました。")
# idToken取得
try:
    req_post = requests.post(
        f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}"
    )
    idToken = req_post.json()["idToken"]
except Exception:
    print("idTokenの取得に失敗しました。")
print("API使用の準備が完了しました。")
# ===============================================================
# 上場銘柄一覧
# ===============================================================
headers = {"Authorization": "Bearer {}".format(idToken)}
urlPath = "https://api.jquants.com/v1/listed/info"
req = requests.get(urlPath, headers=headers)

# 取得結果
result = req.json()

infos = result["info"]

print(infos[0])

# company_names = [d.get("CompanyName") for d in infos]
