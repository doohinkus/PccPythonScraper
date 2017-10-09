import urllib2
import time
import csv
from bs4 import BeautifulSoup, SoupStrainer
# set up columns for file
with open('books.csv', 'r+') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "ISBN"])
    f.close()
# loop through eight pages
url = "https://www.arcadiapublishing.com/Search?searchText=&seriesfacet=Images+of+America&StateFacet=Oregon&page="
books = {}
buy_books = {}
for i in range(8):
    # build url
    page = urllib2.urlopen(url + str(i))
    # parse page
    soup = BeautifulSoup(page, 'lxml')
    # find links/titles, the links contain the isbn!!!!
    links = soup.find_all('a', {'class' : 'search-title'})

    for link in links:
        # grab isbn from link url by splitting url into an array
        isbn = link['href'].split('/')
        # add isbn and title to books dictionary
        books[isbn[2]] = link.text.strip()

# loop through books
# search pcc by isbn
# if results are 0, add to buy books list
count = 0
for key in books:
    pcc_url = "http://alliance-primo.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?fn=search&ct=search&initialSearch=true&mode=Advanced&tab=default_tab&indx=1&dum=true&srt=rank&vid=PCC&frbg=&tb=t&vl%28401499236UI0%29=isbn&vl%28401499236UI0%29=title&vl%28401499236UI0%29=isbn&vl%281UIStartWith0%29=contains&vl%28freeText0%29=" +key + "&vl%28boolOperator0%29=AND&vl%28401499248UI1%29=any&vl%28401499248UI1%29=title&vl%28401499248UI1%29=any&vl%281UIStartWith1%29=contains&vl%28freeText1%29=&vl%28boolOperator1%29=AND&vl%28401499252UI2%29=any&vl%28401499252UI2%29=title&vl%28401499252UI2%29=any&vl%281UIStartWith2%29=contains&vl%28freeText2%29=&vl%28boolOperator2%29=AND&vl%28D309595628UI3%29=all_items&vl%28743647703UI4%29=all_items&vl%28700666352UI5%29=all_items&vl%28309595632UI6%29=00&vl%28309595633UI6%29=00&vl%28309595634UI6%29=Year&vl%28309595635UI6%29=00&vl%28309595636UI6%29=00&vl%28309595637UI6%29=Year&scp.scps=scope%3A%28PCC%29&Submit=Search"
    pcc_page = urllib2.urlopen(pcc_url)
    # sleep to avoid connection reset--max is 20 connections
    count += 1
    print (count%3)
    if (count % 3 == 0):
        time.sleep(9)
    # parse page
    pcc_soup = BeautifulSoup(pcc_page, 'lxml')
    # find links/titles, the links contain the isbn!!!!
    pcc_result = pcc_soup.find('div', {'id' : 'resultsNumbersTile'})
    if (int(pcc_result.h1.em.text.strip()) == 0):
        print (pcc_result.h1.em.text.strip(), key, books.get(key))
        # write info to csv
        with open('buy_books.csv', 'a') as f:
            writer = csv.writer(f)
            # isbn is the third element in the split array
            writer.writerow([key, books.get(key)])
            f.close()
