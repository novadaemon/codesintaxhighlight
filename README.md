# @CodeSintaxHightLigth

**@CodeSintaxHightLight** helps you to format messages with programming language code

## Requirements

You need to have python installed in your system

https://www.python.org/downloads/

### Install required libraries

`pip install-r requirements.txt`

### Set configuration variables

Create a file named `.env` in project directory root

Add the below variables:

```
TOKEN='YourTelegramBotToken'
HCTI_API_USER_ID='32291e70-0d8f-47b1-915e-f14f9bc370f34'
HCTI_API_KEY='046bc5c2-62a3-419a-873c-e3994ff54adfr'
```

**@CodeSintaxHightLight** use https://hcti.io/ API to generate an image with formatted message

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



## Screenshot

![screenshot](screenshot.png)