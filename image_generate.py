from flask import Flask , request ,jsonify

import os
import openai
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from IPython.display import Image, display

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

os.environ["OPENAI_API_KEY"] ="api_key"

llm = ChatOpenAI(api_key = os.environ['OPENAI_API_KEY'])

def generateImage(description):
    image_url = DallEAPIWrapper().run(description)
    return (image_url)

app = Flask(__name__)
  
@app.route('/image/generate',methods = ['POST'])


def post_image_generator():
    data = request.get_json()
    description = data.get('description')

    result = generateImage(description)

    return jsonify({"It is the image of ": description, "image_url": result})

if __name__ == '__main__':
    app.run(debug=True)
