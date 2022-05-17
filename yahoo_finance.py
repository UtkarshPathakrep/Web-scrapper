import requests

url = "https://query1.finance.yahoo.com/v1/finance/screener?crumb=SizE.5UDs8z&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com"

# curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -XPOST "https://gorest.co.in/public/v2/users/123" -d '{"name":"Allasani Peddana", "email":"allasani.peddana@15ce.com", "status":"active"}'

headers = {
    "Content-Type":"application/json",
    "Content":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
}

payload = {
    "offset": "50",
    "size": "100",
    "sortField": "companyshortname",
    "sortType": "asc",
    "quoteType": "EQUITY"
}

session = requests.Session()
r = session.post(url,headers=headers,data=payload)
print(r)