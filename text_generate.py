from flask import Flask, request, jsonify, send_from_directory
import os
import openai
from langchain_community.llms import OpenAI
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import PyPDF2

os.environ['OPEN_API_KEY'] = "API_KEY"

llm = ChatOpenAI ( api_key = os.environ['OPEN_API_KEY'],
                  model = "gpt-4o")


pdf = "C:/Users/Kaurj/Downloads/Comprehension passage.pdf"


prompt = PromptTemplate(input_variables=["Question","content"],
                        template="Based on the following content : {content}, Answer the question : {Question}")


chain = LLMChain(llm=llm,prompt=prompt)


def read_file_path(file_path):
    text_content = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text_content += page.extract_text()
    return text_content

def generate(Question,content):  
    result = chain.run({"Question": Question, "content": content})
    return result
        
app = Flask(__name__)
@app.route('/answer/generator',methods = ['POST'])
 
def post_ans_gen():
    data = request.get_json()
    Question = data.get('Question')
    content = read_file_path(pdf)
   
    result = generate(Question,content)
    return jsonify(f"Your answer is : {result}")
   
if __name__ == '__main__':
    app.run(debug=True)


