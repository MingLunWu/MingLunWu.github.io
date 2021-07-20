import os
import json
private_key = os.environ['GOOGLE_CLOUD_PRIVATE_KEY']

data = {
  "type": "service_account",
  "project_id": "personal-blog-278509",
  "private_key_id": "1601b8241698a340f19072b6ff34490df80d4ae3",
  "private_key": private_key,
  "client_email": "minglunwu@personal-blog-278509.iam.gserviceaccount.com",
  "client_id": "113191363139112282827",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/minglunwu%40personal-blog-278509.iam.gserviceaccount.com"
}

with open('./output/personal-blog-278509-1601b8241698.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)