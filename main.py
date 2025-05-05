from requests import post,get
URL = "http://127.0.0.1:8000"
if __name__ == "__main__":
    res = post(URL+"/shorten",json={
        "url":"https://www.instagram.com/"
    })
    print(res.status_code)
    res_json = res.json()
    res_url = get(f"{URL}/shortUrl/{res_json["id"]}")
    
    print(res_url.status_code)
    print(res_url.json())