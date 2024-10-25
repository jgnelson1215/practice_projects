''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer", methods = ['GET'])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Check if the request method is POST (form submission)
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    if label == None:
        return "I am sorry, I cannot interpret the text that you have entered."
    label = label.split("_")[1]
    score = response['score']
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
