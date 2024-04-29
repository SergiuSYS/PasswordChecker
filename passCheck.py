import requests
import sys
import hashlib

def request_api_data(HashPass):
    url = 'https://api.pwnedpasswords.com/range/' + HashPass
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching:{res.status_code},check the api and start agane')
    return res

def get_passowrds_counts(hashes,myhash):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for h,count in hashes:
            if h == myhash:
                return count
        return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    res = request_api_data(sha1password[:5])
    return get_passowrds_counts(res,sha1password[5:])

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times')
        else:
            print(f"{password} was not found")
    return 'done'
main(sys.argv[1:])

