import logging
import flask
from flasgger import Swagger
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from summarizer import Summarizer

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Initialize the Flask application
application = Flask(__name__)

application.config['ALLOWED_EXTENSIONS'] = set(['pdf'])
application.config['CONTENT_TYPES'] = {"pdf": "application/pdf"}
application.config["Access-Control-Allow-Origin"] = "*"


CORS(application)

swagger = Swagger(application)

def clienterror(error):
    resp = jsonify(error)
    resp.status_code = 400
    return resp


def notfound(error):
    resp = jsonify(error)
    resp.status_code = 404
    return resp


@application.route('/v1/summarize', methods=['POST'])
def summarize_text():
    """Run news summarization given input raw text
        ---
        parameters:
          - text: body of the news article
            in: body
            schema:
              id: text
              required:
                - text
              properties:
                text:
                  type: string
            description: the required text for POST method
            required: true
        definitions:
          SummaryResponse:
          Project:
            properties:
              status:
                type: string
              ml-result:
                type: object
        responses:
          40x:
            description: Client error
          200:
            description: Summary generation response
            examples:
                          [
{
  "status": "success",
  "Summary": "Joe biden is elected as new president of the US"
},
{
  "status": "error",
  "message": "Exception caught"
},
]
        """
    json_request = request.get_json()
    if not json_request:
        return Response("No json provided.", status=400)
    text = json_request['text']
    if text is None:
        return Response("No text provided.", status=400)
    else:
        model = Summarizer()
        result = model(text, num_sentences=1)
        return flask.jsonify({"status": "success", "text": result})





if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)
