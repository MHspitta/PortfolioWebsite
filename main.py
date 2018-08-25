from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import csv

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-control"] = "no cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
