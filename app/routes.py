from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, current_app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/book-a-table', methods=['POST'])
def book_table():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    date = request.form.get('date', '').strip()
    time = request.form.get('time', '').strip()
    people = request.form.get('people', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not phone or not date or not time or not people:
        flash('Semua field wajib diisi!', 'error')
        return redirect(url_for('main.home'))  

    import re
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        flash('Format email tidak valid!', 'error')
        return redirect(url_for('main.home'))

@main.route('/pesan')
def pesan():
    return render_template('pesan.html')
