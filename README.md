# Token-api
A api for the token of miaou-bot (simple)
## Authorization
If you get authorized by Noémie to have access to creating content to the bot she will give you an api key
<br>
Just do a get request to https://tokenapi.miaou-discord-bot.repl.co/token with this as payload {"token": your key}
<br>
it's gonna return you {"token": token} with a 200 request code.
## Exemple
Javascript
```js
const key = 'your key';

const payload = {
  token: key
};

const queryString = Object.keys(payload)
  .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(payload[key]))
  .join('&');

const url = 'https://tokenapi.miaou-discord-bot.repl.co/token?' + queryString;

fetch(url)
  .then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error(`Request failed with status code ${response.status}`);
  })
  .then(data => {
    const Token = data.token;
  })
  .catch(error => {
    console.error('Error:', error);
  });
```
Python
```py
import requests
key = 'your key'

payload = {
  'token': key
}
url = 'https://tokenapi.miaou-discord-bot.repl.co/token'
response = requests.get(url, params=payload)

try:
  Token = response.json()['token']
except:
  exit("Request failed with status code ${response.status_code")
```
