import requests
import json
from colorama import init
init()

term = input('what trademark do you want to search for?\n')
print(f'\nSearch Term: {term}')

response = requests.get(f'https://www.ic.gc.ca/app/api/ic/ctr/trademarks/search/.json?dataBeanJson=%7B%22selectField1%22%3A%22tm%22%2C%22textField1%22%3A%22{term}%22%2C%22category%22%3A%22%22%2C%22type%22%3A%22%22%2C%22status%22%3A%22%22%2C%22viennaField%22%3A%5B%5D%2C%22searchDates%22%3A%5B%5D%2C%22selectMaxDoc%22%3A%22500%22%2C%22language%22%3A%22eng%22%7D&draw=1&columns%5B0%5D%5Bdata%5D=applicationNumber&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=intrnlRegNum&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=title&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=tmType&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=statusDescEn&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=niceClasses&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=mediaUrls&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=25&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1590385412559')
# response2 = requests.get(f'https://www.ic.gc.ca/app/api/ic/ctr/trademarks/search/.json?dataBeanJson=%7B%22selectField1%22%3A%22tm%22%2C%22textField1%22%3A%22{term}%22%2C%22category%22%3A%22%22%2C%22type%22%3A%22%22%2C%22status%22%3A%22%22%2C%22viennaField%22%3A%5B%5D%2C%22searchDates%22%3A%5B%5D%2C%22selectMaxDoc%22%3A%22500%22%2C%22language%22%3A%22eng%22%7D&start=0&length=25')

responsejson = response.json()

recordsTotal = responsejson['recordsTotal']
print(f'Number of Records: {recordsTotal}')



print('Titles:')
i=0
for result in responsejson['data']:
    i+=1
    title = result['title']
    heading = result['heading']
    print(f'\t{i}.) {title}; heading: {heading}')
    