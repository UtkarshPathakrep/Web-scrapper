import requests
import json


count = 100
offset = 100
crumb = "8XE%2Flw5Ktvx"
region = "US"

url = "https://query1.finance.yahoo.com/v1/finance/screener?crumb={}&lang=en-US&region={}&formatted=true&corsDomain=finance.yahoo.com".format(crumb,region)

# curl 'https://query2.finance.yahoo.com/v1/finance/screener?crumb=8XE%2Flw5Ktvx&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://finance.yahoo.com/gainers?count=100&offset=300' -H 'Content-Type: application/json' -H 'Origin: https://finance.yahoo.com' -H 'Connection: keep-alive' -H 'Cookie: A1=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI; A3=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI; B=5rgucghh2jo8h&b=3&s=e9; GUC=AQEBBgFihedjSkIh1wTJ; A1S=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI&j=WORLD; GUCS=ARNuWZxU; cmp=t=1652856970&j=0&u=1---; thamba=1' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'TE: trailers' --data-raw '{"offset":300,"size":100,"sortField":"percentchange","sortType":"DESC","quoteType":"EQUITY","query":{"operator":"AND","operands":[{"operator":"GT","operands":["percentchange",3]},{"operator":"eq","operands":["region","us"]},{"operator":"or","operands":[{"operator":"BTWN","operands":["intradaymarketcap",2000000000,10000000000]},{"operator":"BTWN","operands":["intradaymarketcap",10000000000,100000000000]},{"operator":"GT","operands":["intradaymarketcap",100000000000]}]},{"operator":"gt","operands":["dayvolume",15000]}]},"userId":"","userIdType":"guid"}'

headers = {
    "Content-Type":"application/json",
    "Content":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Referer": "https://finance.yahoo.com/gainers?count={}&offset={}".format(count,offset),
    "Accept-Encoding":"gzip, deflate, br",
    "Origin":"https://finance.yahoo.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Cookie": "A1=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI; A3=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI; B=5rgucghh2jo8h&b=3&s=e9; GUC=AQEBBgFihedjSkIh1wTJ; A1S=d=AQABBBHhKWICEBdK067cNFlTmd3nroTMw10FEgEBBgHnhWJKY1lQb2UB_eMBAAcIEeEpYoTMw10&S=AQAAAg8myhgJVK7Of0EscPdF0hI&j=WORLD; GUCS=ARNuWZxU; cmp=t=1652856970&j=0&u=1---; thamba=1"
}

payload = {
    "offset": offset,
    "size": count,
    "sortField": "percentchange",
    "sortType": "DESC",
    "quoteType": "EQUITY",
    "query": {
        "operator": "AND",
        "operands": [{
            "operator": "gt",
            "operands": ["intradayprice", 0]
        }]
    },
    "userId": "",
    "userIdType": "guid"
}

# session = requests.Session()
r = requests.post(url,headers=headers,data=json.dumps(payload))
print(json.dumps(r.json(),indent=4))
with open('test_2.json','w') as f:
    json.dump(r.json(),f,indent=4)

"""
- regularMarketPreviousClose
- regularMarketOpen
- regularMarketVolume
- regularMarketDayRange
- fiftyTwoWeekRange
- symbol
- language
- marketCap
- market
- shortName
- exchange
- region
- displayName
- quoteType
- currency
- sharesOutstanding
- regularMarketPrice
- longName
- total (count) 
"""