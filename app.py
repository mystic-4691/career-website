
from flask import Flask, render_template, request, redirect, url_for, session

app=Flask(__name__)

@app.route('/')
def helloworld():
  return "Hello rajesh, hi"


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)