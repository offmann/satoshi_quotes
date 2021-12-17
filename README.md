```
       _____       __             __    _    ____              __               
      / ___/____ _/ /_____  _____/ /_  (_)  / __ \__  ______  / /____  _____    
      \__ \/ __ `/ __/ __ \/ ___/ __ \/ /  / / / / / / / __ \/ __/ _ \/ ___/    
     ___/ / /_/ / /_/ /_/ (__  ) / / / /  / /_/ / /_/ / /_/ / /_/  __(__  )     
    /____/\__,_/\__/\____/____/_/ /_/_/   \___\_\__,_/\____/\__/\___/____/      
                                                                                
                                                                                 
```


This is a python crawler that scrape satoshi nakamoto quotes from https://satoshi.nakamotoinstitute.org/quotes/   
    
Satoshi is the emblematic creator (creators) of bitcoin. He authored the bitcoin white paper, and created and deployed bitcoin's original reference implementation. As part of the implementation, Nakamoto also devised the first blockchain database. Nakamoto was active in the development of bitcoin up until December 2010. Many people have claimed, or have been claimed, to be Nakamoto.

Nakamoto stated that work on the writing of the code for bitcoin began in 2007. On 18 August 2008, he or a colleague registered the domain name bitcoin.org, and created a web site at that address. On 31 October, Nakamoto published a white paper on the cryptography mailing list at metzdowd.com describing a digital cryptocurrency, titled "Bitcoin: A Peer-to-Peer Electronic Cash System".

On 9 January 2009, Nakamoto released version 0.1 of the bitcoin software on SourceForge, and launched the network by defining the genesis block of bitcoin (block number 0), which had a reward of 50 bitcoins.Embedded in the coinbase transaction of this block is the text: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", citing a headline in the UK newspaper The Times published on that date. This note has been interpreted as both a timestamp and a derisive comment on the alleged instability caused by fractional-reserve banking. 

Nakamoto continued to collaborate with other developers on the bitcoin software until mid-2010, making all modifications to the source code himself. He then gave control of the source code repository and network alert key to Gavin Andresen, transferred several related domains to various prominent members of the bitcoin community, and stopped his recognized involvement in the project.

Nakamoto owns between 750,000 and 1,100,000 bitcoin. As of November 2021, that puts his net worth at up to 73 billion US dollars, which would make him the 15th richest person in the world.
    
The quotes are scraped are organized by domain
    

#### Requirements
- Python 3.7 or higher.

#### Install pipenv

```Python
    pip install pipenv
```

#### Install requirements
```Python
    cd satoshi_quotes/
```
```Python
    pipenv shell
```
```Python
    pipenv install
```
## In a terminal
```shell
    python satoshi_quotes/crawler.py
```
