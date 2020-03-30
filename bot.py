from flask import Flask, request
import pandas as pd
import book_ratings
import recommendations
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/welcome', methods=['POST'])
def welcome():
    resp = MessagingResponse()
    
    in1 = request.values.get('Body')

    if(in1):
        resp.message("Hi There! Welcome to bookworm! \nWhat are you looking for?\n1. Find info about book\n2. Some Recommedations!\nChoose the option(enter the number)")
    
    in2 = request.values.get('Body')

    return in2

@app.route('/book_name', methods=['POST'])
def book_name(in2):
    if (in2=='1'):
        resp = MessagingResponse()
        resp.message("Enter name of book: ")
    return (str(resp)) 

@app.route('/info', methods=['POST'])
def info(in2):
    if (in2=='1'):
        resp = MessagingResponse()
        resp.message("Enter name of book: ")
        inbMsg = request.values.get('Body').lower()
        book_list = book_ratings.get_matches(inbMsg)

        df = pd.read_csv('clean_books.csv')
    
        for i in book_list:
            resp.message(
                'The book with title' + df['original_title'].iloc[i] + 'written by ' + df['authors'].iloc[i] +'has average user rating of ' + str(df['average_rating'].iloc[i])+'.\n ---------------------------------')
    return str(resp)

@app.route('/rec', methods=['POST'])
def rec(in2):
    if(in2 == '2'):
        resp.message('on which basis you want recommendations?\n1.Author\n2.Tag\n3.content')
        in3 = request.values.get('Body')
        if(in3=='1'):

            in4 = request.values.get('Body')
            answer = recommendations.authors_recommendations(in4)
            resp.message(answer)
        elif(in3=='2'):
            in4 = request.values.get('Body')
            answer = recommendations.tags_recommendations(in4)
            resp.message(answer)
        elif(in3=='3'):
            in4 = request.values.get('Body')
            answer = recommendations.corpus_recommendations(in4)
            resp.message(answer)
        

        



    

if __name__ == '__main__':
    app.run()