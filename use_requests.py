import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code ==200:
        print(f'Sucsess! Response = {response.status_code}')
        print(f'Content {response .text} ')
    else :
        (f'woops, ada kesalahan requests {response.status_code}')
except Exception as e:
   print(f'There is an error, {e}' )
print('Program ended')
