from flask import Flask, render_template
from flask import request

app = Flask(__name__)
from app import routes
