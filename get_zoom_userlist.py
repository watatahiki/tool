import requests

# Zoom APIのエンドポイントと認証情報
api_key = 'Your_API_Key'
api_secret = 'Your_API_Secret'
base_url = 'https://api.zoom.us/v2'
auth_token = None  # 認証トークンは初めはNoneで設定

# 認証トークンの取得
def get_access_token():
    global auth_token
    auth_endpoint = f"{base_url}/oauth/token"
    headers = {
        'Authorization': f'Basic {api_key}:{api_secret}',
        'Content-Type': 'application/json'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_endpoint, headers=headers, json=data)
    if response.status_code == 200:
        auth_token = response.json()['access_token']
    else:
        print("Failed to get access token")

# ユーザー一覧を取得する関数
def get_user_list():
    if auth_token is None:
        get_access_token()
    if auth_token:
        user_endpoint = f"{base_url}/users"
        headers = {
            'Authorization': f'Bearer {auth_token}'
        }
        response = requests.get(user_endpoint, headers=headers)
        if response.status_code == 200:
            users = response.json()['users']
            return users
        else:
            print("Failed to get user list")
            return None

# メイン処理
if __name__ == '__main__':
    users = get_user_list()
    if users:
        print("User List:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['first_name']} {user['last_name']}, Email: {user['email']}")