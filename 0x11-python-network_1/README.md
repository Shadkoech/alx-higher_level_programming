# 0x11. Python - Network #1

Herein are a number of practice exercises on How to fetch Internet resources using the urllib Package. Basically, urrlib.request is a Python module used for fetching URLs (Uniform Resource Locators). The module offers a simple interface in the form of urlopen function. The key objective is to create a knowledge base to answer questions such as:

	- How to fetch internet resources using the Python package urrlib
	- How to decode urllib body response
	- How to use the Python package requests (A substitute to urllib)
	- How to make HTTP GET request
	- How to make HTTP POST/PUT/etc. request
	- How to fetch JSON resources




## Task 0: What's my status? #0

File:

	- 0-hbtn_status.py
Python script that fetches https://alx-intranet.hbtn.io/status
- You must use the package urllib
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed like the following example (tabulation before -)
- You must use a with statement



## Task 1: Response header value #0

File:

	- 1-hbtn_header.py
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
- You must use the packages urllib and sys
- You are not allow to import packages other than urllib and sys
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a with statement



## Task 2: POST an email #0

File:

	- 2-post_email.py
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement



## Task 3: Error code #0

File:

	- 3-error_code.py
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
- You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
- You must use the packages urllib and sys
- You are not allowed to import other packages than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement



## Task 4: What's my status? #1

File:

	- 4-hbtn_status.py
Python script that fetches https://alx-intranet.hbtn.io/status
- You must use the package requests
- You are not allow to import packages other than requests



## Task 5: Response header value #1

File:

	- 5-hbtn_header.py
Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
- You must use the packages requests and sys
- You are not allow to import other packages than requests and sys
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)



## Task 6:POST an email #1

File:

	- 6-post_email.py
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
- The email must be sent in the variable email
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to error check arguments passed to the script (number or type)



## Task 7:Error code #1

File:

	- 7-error_code.py
Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)



## Task 8:Search API

File:

	- 8-json_api.py
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>

Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys



## Task 9:My GitHub!

File:

	- 10-my_github.py
Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
- You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a personal access token as password)
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
