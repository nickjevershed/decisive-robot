import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    #get question from url ('?q=this is a question')
    #call decisiverobot.ask(question)
    #get the html content from a file
    #inject the answer into the html content
    #return it
    #
    #Or get fancy and have the client call ask() via a json api.
    #Still allow the url get ('q?=') to be used (via pure client side code) so that
    #hyperlinking to questions will work
    #Hmm do we want to log all questions...
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)