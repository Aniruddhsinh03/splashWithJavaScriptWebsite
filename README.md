# splashWithJavaScriptWebsite

This is a Scrapy project to scrape quotes,tags and author information from  http://quotes.toscrape.com/js/.

This project is only meant for educational purposes.


## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'Author': 'Douglas Adams',
        'Comment': '“I may not have gone where I intended to go, but I think I ...”',
        'Tags': ['life', 'navigation']
       
    }


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    splashWithJsWebsite

Spider extract the data from quotes page and visit author hyperlink and extract auther infomation also.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl splashWithJsWebsite

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl splashWithJsWebsite -o output.json
