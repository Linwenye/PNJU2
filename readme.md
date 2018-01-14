## Introduction

**Auto login to the school network**  

It's written just because the one written using Scrapy is too slow for such a really really easy task, which only include three to four lines of code.

## If you want to use it

1. Download the source code

2. Edit the bat file, configure the path to where you store the source code

3. Add file naming config.py under PNJU2/ with content like

   > 'username' = '151250093'
   >
   > 'password' = '88888'

4. Now click the bat file, it can automatically connect the p.nju.edu.cn. And if you are willing to, you can set the bat file to be run after the computer starts up.


## Requirement

Python3 environment with requests is needed.

If you already installed Python3, just install requests using

> $ pip install requests

