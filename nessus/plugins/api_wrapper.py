import requests
from json import JSONDecodeError
import urllib3

urllib3.disable_warnings()


def grab_headers():
    access_key = ''
    secret_key = ''
    return {'Content-type': 'application/json', 'X-ApiKeys': 'accessKey=' + access_key + ';secretKey=' + secret_key}


def request_data(method, url_mod, **kwargs):

    # set the Base URL
    url = "https://192.168.128.67:8834"

    # check for params and set to None if not found
    try:
        params = kwargs['params']
    except KeyError:
        params = None

    # check for a payload and set to None if not found
    try:
        payload = kwargs['payload']
    except KeyError:
        payload = None

    # Retry the download three times
    for x in range(1, 3):
        try:
            r = requests.request(method, url + url_mod, headers=grab_headers(), params=params, json=payload, verify=False)
            if r.status_code == 200:
                return r

            if r.status_code == 202:
                # This response is for some successful posts.
                print("\nSuccess!\n")
                break
            elif r.status_code == 404:
                print('\nCheck your query...I can\'t find what you\'re looking for {}'.format(r))
                return r.json()
            elif r.status_code == 429:
                print("\nToo many requests at a time...\n{}".format(r))
                break
            elif r.status_code == 400:
                print("\nThe object you tried to create may already exist\n")
                print("If you are changing scan ownership, there is a bug where 'empty' scans won't be moved")
                break
            elif r.status_code == 403:
                print("\nYou are not authorized! You need to be an admin\n{}".format(r))
                break
            elif r.status_code == 409:
                print("API Returned 409")
                break
            elif r.status_code == 504:
                print("\nOne of the Threads and an issue during download...Retrying...\n{}".format(r))
                break
            else:
                print("Something went wrong...Don't be trying to hack me now {}".format(r))
                break
        except ConnectionError:
            print("Check your connection...You got a connection error. Retying")
            continue
        except JSONDecodeError:
            print("Download Error or User enabled / Disabled ")
            continue
