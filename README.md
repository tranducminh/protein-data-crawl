# protein-data-crawl

## Init environment

### Install anaconda
[Anaconda](https://www.anaconda.com/)
Create virtual workspace

## Install scrapy
```
chsh /bin/bash
conda activate {virtual_workspace_name}
conda install -c conda-forge scrapy pylint autopep8 -y
```
## Crawl data
```scrapy crawl proteins -o proteins.json```
