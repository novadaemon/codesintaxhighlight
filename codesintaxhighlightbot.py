from telegram.ext import Updater
from telegram.ext import CommandHandler
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re
import requests

TOKEN = "1386943447:AAGb6qFs8gOB0m_TIWzcJaEGWOAWIhTjnRg"

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = '32291e70-0d8f-47b1-915e-f14f9bc380d2'
HCTI_API_KEY = '046bc5c2-62a3-419a-873c-e3994ff54fae'

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

langs = ['php','python', 'html']

def helpCmd(update, context):
    text = """
*@CodeSintaxHightLight helps you to format messages with programming language code.*
*Usage:*
```
/format@CodeSintaxHightLight python
numbers = [1,2,3,4,5,6]
for number in numbers:
    print(number)
```    
"""

    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text=text)

def langsCmd(update, context):
    text = ''
    for i in range(len(langs)):
        text += '<b>'+str(i+1)+'.</b> '+langs[i] +'\r\n'

    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='HTML', text=text)

def formatCmd(update, context):
    try:
        msg = update['message']['text']

        m = re.search('\s.+\\n', msg)

        lang = m.group(0).strip()

        if(lang not in langs):
            context.bot.send_message(chat_id=update.effective_chat.id, text="The format is not supported!") 
            return   
        
        code = msg.replace('/format@CodeSintaxHighLightBot '+lang+'\n', '')

        lexer = get_lexer_by_name(lang, stripall=False)
        formatter = HtmlFormatter(linenos=True)

        html = highlight(code, lexer, formatter)
        css = formatter.get_style_defs('.highlight')

        data = { 
            'html': html,
            'css':css 
        }

        image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

        url = image.json()['url']

        context.bot.send_message(chat_id=update.effective_chat.id, text=url)

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="An error has ocurred parsing the message")


help_handler = CommandHandler('help', helpCmd)
langs_handler = CommandHandler('langs', langsCmd)
format_handler = CommandHandler('format', formatCmd)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(langs_handler)
dispatcher.add_handler(format_handler)


updater.start_polling()