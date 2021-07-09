# @CodeSintaxHighLigthBot

**@CodeSintaxHighLightBot** helps you to format messages with programming language code

## Requirements

You need to have python installed in your system

https://www.python.org/downloads/

### Install required libraries

`pip install -r requirements.txt`

### Set configuration variables

Create a file named `.env` in project directory root

Add the below variables:

```
TOKEN='YourTelegramBotToken'
HCTI_API_USER_ID='YourHCTIAPIUserID'
HCTI_API_KEY='YourHCTIAPIKey'
```

**@CodeSintaxHighLightBot** use https://hcti.io/ API to generate an image with formatted message

## Run

`python codesintaxhighlightbot.py`

## Commands

- **/help** Show bot's help
- **/langs** Show supported langs
- **/format** Format the code

## Format command usage

For usage `/format` command use the below sintax

```python
/format python

def function hello():
    print('hello')
```

## Talk to bot
https://telegram.me/CodeSintaxHighLightBot
## Screenshot

![screenshot](screenshot.png)