from requests import post,get
URL = "http://127.0.0.1:8000"
if __name__ == "__main__":
    res = post(URL+"/shorten",json={
        "url":"https://www.instagram.com/"
    })
    print(res.status_code)
    res_json = res.json()
    print(res_json)
    res_url_1 = get(f"{URL}/shortUrl/{res_json["id"]}")
    
    print(res_url_1.status_code)
    # print(res_url_1.json())
    
    res_url_2 = get(f"{URL}/shortUrl/{str(2)}")
    print(res_url_2.status_code)
    print(res_url_2.json())