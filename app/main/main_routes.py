from flask import render_template, redirect, url_for, flash, request, session, jsonify, copy_current_request_context
from ..extensions import db, User, Reference, Container, Cargo, cache
from . import main

@main.route('/')
def index():
    return render_template('main/home.html')