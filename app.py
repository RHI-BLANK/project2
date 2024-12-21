from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session and flash messages

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Replace with your email password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        msg = Message('New Contact Form Submission', sender='your_email@example.com', recipients=['your_email@example.com'])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        mail.send(msg)
        flash('Thank you for your message, ' + name + '!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
