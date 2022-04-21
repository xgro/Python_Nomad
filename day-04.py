# import
import requests
import os

http = 'http://'
https = 'https://'
com = '.com'

while True:
    print('Welcome to IsItDown.py!')
    print('Please write a URLs you want to check. (separated by comma)')

    urls = input()
    urls = urls.replace(" ","").split(',')

    for url in urls:
        if com not in url:
            print(f'{url} is not a vaild URL.')
            continue
            
        if http not in url:
            if https not in url:
                url = http + url

        try:       
            res = requests.get(url)

        except requests.exceptions.RequestException:
            print(f'{url} is down!')

        else:
            print(f'{url} is up!')
        # print(res.status_code)

        # print(urls)

    while True:
        res = input('Do you want to start over? y/n ')
        if res == 'y':
            break
        elif res == 'n':
            break
        else:
            print("That's not a vaild answer")
            pass
        # print(urls)

    if res == 'y':
        os.system('clear')
    elif res == 'n':
        print("k, bye!")
    break


