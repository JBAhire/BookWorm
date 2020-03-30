from flask import Flask, request
import pandas as pd
import book_ratings
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    #hey = MessagingResponse()
    inbMsg = request.values.get('Body')
    book_list = book_ratings.get_matches(inbMsg)

    #rec = recommendations.corpus_recommendations(inbMsg)

   # hey.message("Recommendations based on your input: \n" + str(rec))


    df = pd.read_csv('clean_books.csv')

    for i in book_list:
        resp.message(
            'Title of the book: ' + df['original_title'].iloc[i] + '\nWritten by: ' + df['authors'].iloc[i] +'\nAverage user rating: ' + str(df['average_rating'].iloc[i])+'\nReviewed by: '+ str(df['work_text_reviews_count'].iloc[i])+' people.\n ---------------------------------------')
    return str(resp)
 

if __name__ == '__main__':
    app.run()