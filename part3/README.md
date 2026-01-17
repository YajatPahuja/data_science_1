# TOPSIS Web Service

A Flask web application for TOPSIS multi-criteria decision analysis that sends results via email.

## Setup

1. Install dependencies:
```bash
pip install flask pandas numpy
```

2. Configure email in `app.py`:
```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
```

**Note:** Use Gmail App Password, not your regular password. Generate one at: https://myaccount.google.com/apppasswords

3. Run the application:
```bash
python app.py
```

4. Open http://127.0.0.1:5000 in your browser

## Usage

1. Upload a CSV file
2. Enter weights (comma-separated, e.g., `1,1,1,1`)
3. Enter impacts (comma-separated, `+` or `-`, e.g., `+,+,-,+`)
4. Enter your email address
5. Click Submit
6. Check your email for results

## Input File Format

CSV file with:
- First column: Alternative names
- Remaining columns: Numeric criteria values

Example:
```
Fund Name,P1,P2,P3,P4
M1,0.67,0.45,6.5,42.6
M2,0.6,0.36,3.6,53.3
```
