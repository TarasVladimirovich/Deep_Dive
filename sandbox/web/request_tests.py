import requests

# payload = {'name': 'Ira', 'position': 'God'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text, end='\n +++++++++++++')
# r = requests.post('https://httpbin.org/post', params=payload)
# print(r.text, end='\n +++++++++++++')
# r = requests.post('https://httpbin.org/post', json=payload)
# print(r.text, end='\n +++++++++++++')
# r = requests.post('https://httpbin.org/post', headers=payload)
# print(r.text, end='\n +++++++++++++')
# r = requests.post('https://httpbin.org/post')
# print(r.text, end='\n +++++++++++++')

try:
    r = requests.get('https://qwertyuytrewq.com')
except requests.exceptions.ConnectionError as e:
    print(f'CONNECTION ERROR!!!\n{e}')
