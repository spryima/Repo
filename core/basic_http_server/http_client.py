from http import client




connection1 = client.HTTPConnection('localhost', 8002)

connection1.request("GET", "/")
answer = connection1.getresponse()
print(answer.status, answer.reason)

data = answer.read()
print(data)


connection1.close()