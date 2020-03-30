from flask import Flask, request
import pandas as pd
import book_ratings
import recommendations
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    inbMsg = request.values.get('Body')
    rec = recommendations.corpus_recommendations(inbMsg)
    df = pd.read_csv('clean_books.csv')
    resp.message('Recommendations based on your input:')
    for i in rec:
        resp.message (df['original_title'].iloc[i+2]+ "\n")
    return str(resp)
 

if __name__ == '__main__':
    app.run()