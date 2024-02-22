#박빙구
#code = https://kauth.kakao.com/oauth/authorize?client_id=ddcfd4509dc2ec690ebb764199ff2247&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends

#박정철
#code = https://kauth.kakao.com/oauth/authorize?client_id=bb6714e8dac2cf258c4d3cc708b8d7ac&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends

import requests 
import json 

#박빙구
rest_api_key = 'ddcfd4509dc2ec690ebb764199ff2247'
#박정철
#rest_api_key = 'bb6714e8dac2cf258c4d3cc708b8d7ac'
redirect_uri = 'https://example.com/oauth' 
url_token = 'https://kauth.kakao.com/oauth/token'
authorize_code = '56lbuGllC3KGFYFfH9xeDCoWjRRxvizAHyPTwPJze-fYqgkETOVWsd-iPm19a8aKPUCtGgorDKgAAAGAW2xVpA' 

try: 
    with open("kakao_token.json","r") as fp: # 기존에 저장된 token 파일이 있는지 찾아봅니다. 
        tokens = json.load(fp) 
        if "error_code" in tokens:
            tokens={} 
except Exception as e:
    print(e) 
    tokens={}
    
if tokens == {}: # 신규 발급이 필요한 경우
    param = { 'grant_type':'authorization_code',
            'client_id':rest_api_key,
            'redirect_uri':redirect_uri,
            'code': authorize_code, # 한번 발급되면 authorize_code는 무효화됩니다. 
            } 
    response = requests.post('https://kauth.kakao.com/oauth/token', data=param)
    tokens = response.json() # token 발급 api로 발급된 정보들을 kakao_token.json 파일에 저장합니다.
    
    if "error_code" in tokens:
        print(tokens["error_code"])
    else: 
        with open("kakao_token.json","w") as fp:
            json.dump(tokens, fp)
            print("파일로 토큰 정보 저장!") 
else: 
    # 기존 발급된 정보가 있을 경우 
    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
        } 
    # access_token_info의 결과가 계속 -401로 돌아옵니다. 추후 수정할 예정입니다.
    response = requests.get('https://kapi.kakao.com/v1/user/access_token_info', headers=headers)
    result = response.json() 
    if "error_code" in result: 
        # -401은 유효하지 않은 값 혹은 유효기간이 지난 토큰일 경우 발생하는 에러입니다. 
        # # api로 token 갱신을 요청합니다. 
        param = { 
                "grant_type":"refresh_token",
                "client_id" : rest_api_key,
                "refresh_token" : tokens["refresh_token"]
                } 
        response = requests.post('https://kauth.kakao.com/oauth/token', data=param)
        new_token = response.json()
        
        # 새로 발급된 token을 다시 저장합니다. 
        if "error_code" in new_token: 
            print("ERROR :", new_token["error_code"])
        else: 
            with open("kakao_token.json", "w") as fp:
                json.dump(new_token, fp)
                print("파일로 새로운 토큰 정보 저장!") 
    else: print("정상 토큰")

