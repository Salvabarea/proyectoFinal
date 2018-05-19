import hashlib
import requests
import json
publica = 'fbc50db8c7ae0952d6c05a78516418fc'
privada = '2b0fdabbb600f543b7070f4dff68443700be7f92'
ts = '1'
hash = hashlib.md5((ts + privada + publica).encode()).hexdigest()

base = 'http://gateway.marvel.com/v1/public/'
personajes = requests.get(base + 'characters',
                          params={'apikey': publica,
                                  'ts': ts,
                                  'hash': hash}).json()
print (personajes['data']['results'])
