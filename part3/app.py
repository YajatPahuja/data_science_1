from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import re

load_dotenv()

app = Flask(__name__)
os.makedirs('uploads', exist_ok=True)
app.secret_key = os.getenv('SECRET_KEY', 'topsis_secret_key')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def topsis(input_file, weights_str, impacts_str):
    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        return None, "Input file must contain three or more columns."

    for col in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            return None, f"Column '{col}' contains non-numeric values."

    num_criteria = df.shape[1] - 1

    try:
        weights = np.array([float(w.strip()) for w in weights_str.split(',')])
    except:
        return None, "Weights must be numeric values separated by commas."

    impacts = [i.strip() for i in impacts_str.split(',')]

    if len(weights) != num_criteria:
        return None, f"Number of weights ({len(weights)}) must match number of criteria ({num_criteria})."

    if len(impacts) != num_criteria:
        return None, f"Number of impacts ({len(impacts)}) must match number of criteria ({num_criteria})."

    for impact in impacts:
        if impact not in ['+', '-']:
            return None, f"Impacts must be either '+' or '-'. Found: '{impact}'"

    matrix = df.iloc[:, 1:].values.astype(float)

    norm = np.sqrt(np.sum(matrix**2, axis=0))
    normalized = matrix / norm

    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for j in range(len(impacts)):
        if impacts[j] == '+':
            ideal_best.append(max(weighted[:, j]))
            ideal_worst.append(min(weighted[:, j]))
        else:
            ideal_best.append(min(weighted[:, j]))
            ideal_worst.append(max(weighted[:, j]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    s_plus = np.sqrt(np.sum((weighted - ideal_best)**2, axis=1))
    s_minus = np.sqrt(np.sum((weighted - ideal_worst)**2, axis=1))

    scores = s_minus / (s_plus + s_minus)
    ranks = scores.argsort()[::-1].argsort() + 1

    df['Topsis Score'] = np.round(scores, 2)
    df['Rank'] = ranks

    return df, None

def send_email(receiver_email, file_path):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "TOPSIS Analysis Results"

    body = "Please find attached your TOPSIS analysis results."
    msg.attach(MIMEText(body, 'plain'))

    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename=result.csv")
        msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)

        file = request.files['file']
        weights = request.form.get('weights', '')
        impacts = request.form.get('impacts', '')
        email = request.form.get('email', '')

        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if not weights:
            flash('Please enter weights')
            return redirect(request.url)

        if not impacts:
            flash('Please enter impacts')
            return redirect(request.url)

        if not email or not validate_email(email):
            flash('Please enter a valid email address')
            return redirect(request.url)

        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result_df, error = topsis(filepath, weights, impacts)

            if error:
                flash(error)
                os.remove(filepath)
                return redirect(request.url)

            result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
            result_df.to_csv(result_path, index=False)

            if send_email(email, result_path):
                flash('Results sent to your email successfully!')
            else:
                flash('Error sending email. Please check email configuration.')

            os.remove(filepath)
            os.remove(result_path)

            return redirect(request.url)
        else:
            flash('Please upload a CSV file')
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
