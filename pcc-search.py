import urllib2
import csv
from bs4 import BeautifulSoup, SoupStrainer

url = "http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?fn=search&ct=search&initialSearch=true&mode=Advanced&tab=default_tab&indx=1&dum=true&srt=rank&vid=PCC&frbg=&tb=t&vl%28401499236UI0%29=isbn&vl%28401499236UI0%29=title&vl%28401499236UI0%29=isbn&vl%281UIStartWith0%29=contains&vl%28freeText0%29=" +"9780738571461" + "&vl%28boolOperator0%29=AND&vl%28401499248UI1%29=any&vl%28401499248UI1%29=title&vl%28401499248UI1%29=any&vl%281UIStartWith1%29=contains&vl%28freeText1%29=&vl%28boolOperator1%29=AND&vl%28401499252UI2%29=any&vl%28401499252UI2%29=title&vl%28401499252UI2%29=any&vl%281UIStartWith2%29=contains&vl%28freeText2%29=&vl%28boolOperator2%29=AND&vl%28D309595628UI3%29=all_items&vl%28743647703UI4%29=all_items&vl%28700666352UI5%29=all_items&vl%28309595632UI6%29=00&vl%28309595633UI6%29=00&vl%28309595634UI6%29=Year&vl%28309595635UI6%29=00&vl%28309595636UI6%29=00&vl%28309595637UI6%29=Year&scp.scps=scope%3A%28PCC%29&Submit=Search"

page = urllib2.urlopen(url)
# parse page
soup = BeautifulSoup(page, 'lxml')
# find links/titles, the links contain the isbn!!!!
result = soup.find('div', {'id' : 'resultsNumbersTile'})
print (result.h1.em.text.strip())


# with open('books.csv', 'r') as info:
#     for row in info:
#         print row
#     info.close()
