# _PCC Python Scraper_

#### _Super simple web scraper that uses BeautifulSoup. I wrote this script for a project that I had to do at PCC. My task was to find all of the books in the "Images of America" series about Portland, OR that were NOT in PCC's collection. My script scrapes the Arcadia Publishing site, grabbing the ISBNs and titles of appropriate books in the series, storing them in a dictionary. Then it iterates through the dictionary an uses the ISBN to search the PCC Online Catalog. The results are parsed. If the title is NOT present, then the ISBN and title are added to a csv file._

#### By _**Rafael Perez**_

## Description

_A python 2.7.x application scrapes two websites for titles in the "Image of America" series from Arcadia Publishing._


## Setup/Installation Requirements (Requires Python 2.7.x)

* _Clone repository._
* _"pip install bs4"._
* _Run "python portland-picture-books.py"._
* _Open buy_books.csv  All titles not owned by PCC will be in the file._

## Known Bugs

_There are no known bugs at this time._

## Support and contact details

_If you have any issue with this code, please contact me._

## Technologies Used

_ES6, Babel, Webpack, Scss, Vanilla JS._

### License

*MIT License*

Copyright (c) 2016 **_Rafael Perez_**
