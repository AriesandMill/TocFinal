
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocBot

API_TOKEN = '388892866:AAGRDwj7cKFmZSl8Sg-QT8wJQ02ygKjFFAE'
WEBHOOK_URL = 'https://3a19c596.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocBot(
    states=[
        'user',
        'North',
        'Mid',
        'South',
        'East',
        'Nfood',
        'Nshop',
        'Nfun',
        'Mfood',
        'Mshop',
        'Mfun',
        'Sfood',
        'Sshop',
        'Sfun',
        'Efood',
        'Eshop',
        'Efun',
        'final'
    ],
    
    transitions=[
        {
            'trigger':'advance',
            'source':'user',
            'dest':'user',
            'conditions':'is_going_to_user'
        },
        # which area to go 
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'North',
            'conditions': 'is_going_to_North'
        },
        
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'Mid',
            'conditions': 'is_going_to_Mid'
        },
        
        {
            'trigger':'advance',
            'source':'user',
            'dest':'South',
            'conditions': 'is_going_to_South'
        },
        
        {
            'trigger':'advance',
            'source':'user',
            'dest':'East',
            'conditions':'is_going_to_East'
        },
# what to do in the area
        #north            
        {
            'trigger':'advance',
            'source':'North',
            'dest':'Nfood',
            'conditions':'is_going_to_Nfood'
        },
        
        {
            'trigger':'advance',
            'source':'North',
            'dest':'Nshop',
            'conditions':'is_going_to_Nshop'
        },
        
        {
            'trigger':'advance',
            'source':'North',
            'dest':'Nfun',
            'conditions':'is_going_to_Nfun'
        },
        #mid
        {
            'trigger':'advance',
            'source':'Mid',
            'dest':'Mfood',
            'conditions':'is_going_to_Mfood'
        },
        
        {
            'trigger':'advance',
            'source':'Mid',
            'dest':'Mshop',
            'conditions':'is_going_to_Mshop'
        },

        {
            'trigger':'advance',
            'source':'Mid',
            'dest':'Mfun',
            'conditions':'is_going_to_Mfun'
        },
        #south
        {
            'trigger':'advance',
            'source':'South',
            'dest':'Sfood',
            'conditions':'is_going_to_Sfood'
        },

        {
            'trigger':'advance',
            'source':'South',
            'dest':'Sshop',
            'conditions':'is_going_to_Sshop'
        },

        {
            'trigger':'advance',
            'source':'South',
            'dest':'Sfun',
            'conditions':'is_going_to_Sfun'
        },

        #east
        {
            'trigger':'advance',
            'source':'East',
            'dest':'Efood',
            'conditions':'is_going_to_Efood'
        },

        {
            'trigger':'advance',
            'source':'East',
            'dest':'Eshop',
            'conditions':'is_going_to_Eshop'
        },

        {
            'trigger':'advance',
            'source':'East',
            'dest':'Efun',
            'conditions':'is_going_to_Efun'
        },
        
        #final
        #continue
        {
            'trigger':'advance',
            'source':[
                'Nfood',
                'Nshop',
                'Nfun',
                'Mfood',
                'Mshop',
                'Mfun',
                'Sfood',
                'Sshop',
                'Sfun',
                'Efood',
                'Eshop',
                'Efun'
                ],
            'dest':'user',
            'conditions':'is_going_to_ques'
        },
        
        #end
        {
            'trigger':'advance',
            'source':[
                'Nfood',
                'Nshop',
                'Nfun',
                'Mfood',
                'Mshop',
                'Mfun',
                'Sfood',
                'Sshop',
                'Sfun',
                'Efood',
                'Eshop',
                'Efun'
                ],
            'dest':'final',
            'conditions':'is_going_to_final'
        }
        
    ],
    initial = 'user',
#    auto_transitions=False,
#    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()

