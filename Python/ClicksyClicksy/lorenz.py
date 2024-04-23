import requests


def send_requests():
    session = requests.Session()

    requests_list = ['start', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'down', 'down', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'down', 'down', 'right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'right', 'right', 'up', 'up', 'up', 'up', 'right', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'right', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']


    for request_url in requests_list:
        while True:
            response = session.get("http://blindmazerevenge.challs.open.ecsc2024.it/maze?direction=" + request_url)
            print(f"GET {request_url}")

            if "busy" in response.text:
                continue
            else:
                break

    print(response.cookies)
    print(response.headers)
    print(response.status_code)
    print(response.text)

send_requests()