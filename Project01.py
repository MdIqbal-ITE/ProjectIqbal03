import requests as req

url = ("http://192.168.150.135/index.php")
r = req.get(url)
p = r.status_code == req.codes.ok

# To return an "OK" status if request is successful
if p == True:
    print("Status_Ok")
    print(r.status_code)
else:
    print("Failed")

xheaders = {'User-Agent': 'Mobile'}
xy = req.head(headers=xheaders, url=(url))
print("Headers:")
print("**********")
for h in xy.headers:
    print("\t ", h, ":", xy.headers[h])
print("**********")
