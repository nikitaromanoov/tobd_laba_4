from ansible_vault import Vault
import json

vault = Vault("qwerty123")
data = vault.load(open("password.json").read())


print(data)
print(data.keys())
