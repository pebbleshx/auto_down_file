 # Auto login with name and passwd
 # download with a link

import requests
from requests.auth import HTTPBasicAuth

def main(down_url, out_file):
    
    username = 'urname'
    password = 'urpassword'


    r = requests.get(down_url, auth=HTTPBasicAuth(username, password))

    # save to a file, if zip write out as binary
    open(out_file, 'wb').write(r.content)

if __name__ == '__main__':
    main('http://www.theweb.com', 'my_file.zip')
