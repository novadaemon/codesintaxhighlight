from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from decouple import config
import re
import requests


TOKEN = config('TOKEN')
HCTI_API_USER_ID = config('HCTI_API_USER_ID')
HCTI_API_KEY = config('HCTI_API_KEY')

app = ApplicationBuilder().token(TOKEN).build()

langs = ['php','python', 'html', 'css']


async def helpCmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = """
*@CodeSintaxHightLight helps you to format messages with programming language code.*
*Usage:*
```
/format python
numbers = [1,2,3,4,5,6]
for number in numbers:
    print(number)
```
"""
    await update.message.reply_text(text, parse_mode='Markdown')

async def langsCmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ''
    for i in range(len(langs)):
        text += '<b>'+str(i+1)+'.</b> '+langs[i] +'\r\n'

    await update.message.reply_text(text, parse_mode='HTML')

async def formatCmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        msg = update['message']['text']

        m = re.search('\\s.+\\n', msg)

        lang = m.group(0).strip()

        if(lang not in langs):
            await update.message.reply_text("The format is not supported!")
            return   
        
        code = msg.replace('/format@CodeSintaxHighLightBot '+lang+'\n', '')
        code = msg.replace('/format '+lang+'\n', '')

        lexer = get_lexer_by_name(lang, stripall=False)
        formatter = HtmlFormatter(linenos=True)

        html = highlight(code, lexer, formatter)
        css = formatter.get_style_defs('.highlight')

        data = { 
            'html': html,
            'css':css 
        }

        image = requests.post(url = "https://hcti.io/v1/image", data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

        url = image.json()['url']

        await update.message.reply_text(url)
    except:
        await update.message.reply_text("An error has ocurred parsing the message")

app = ApplicationBuilder().token(TOKEN).build()        

app.add_handler(CommandHandler("help", helpCmd))
app.add_handler(CommandHandler("langs", langsCmd))
app.add_handler(CommandHandler("format", formatCmd))


app.run_polling()