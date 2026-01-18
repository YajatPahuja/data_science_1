# Email Sending Flow - What Happens When You Click "Submit"

## Overview
When a user fills out the form and clicks "Submit", here's the complete flow of what happens in your application.

## Step-by-Step Flow

### 1. **Form Submission** (Frontend)
- User fills out the form with:
  - CSV file upload
  - Weights (e.g., `1,1,1,1`)
  - Impacts (e.g., `+,+,-,+`)
  - Email address (e.g., `akshkhurana.tiet@gmail.com`)
- User clicks "Submit" button
- Form sends POST request to `/` route

### 2. **Request Validation** (Backend - `app.py` line 169-179)
```python
# Checks performed:
- File is present and not empty
- Weights are provided
- Impacts are provided  
- Email format is valid (regex validation)
- File is a CSV file
```

**If validation fails:**
- Flash error message shown to user
- Page redirects back to form
- Process stops

### 3. **File Processing** (Backend - line 181-184)
- File is saved to `uploads/` directory
- Filename is sanitized using `secure_filename()`

### 4. **TOPSIS Analysis** (Backend - line 186-191)
- CSV file is read and validated
- TOPSIS algorithm calculates scores and ranks
- Results DataFrame is created with:
  - Original data
  - `Topsis Score` column
  - `Rank` column

**If TOPSIS fails:**
- Error message flashed
- Uploaded file deleted
- Process stops

### 5. **Save Results** (Backend - line 193-194)
- Results DataFrame saved as CSV to `uploads/result_<filename>.csv`

### 6. **Send Email** (Backend - line 196-199)
Calls `send_email(email, result_path)` function:

#### 6.1 **Email Function Validation** (line 103-116)
```python
# Checks:
- RESEND_API_KEY is configured
- Receiver email format is valid
- Result file exists
```

#### 6.2 **Prepare Email** (line 118-136)
```python
# Steps:
1. Read CSV file content (binary)
2. Base64 encode the file content
3. Create email parameters:
   - from: RESEND_FROM_EMAIL (default: onboarding@resend.dev)
   - to: receiver_email
   - subject: "TOPSIS Analysis Results"
   - html: HTML message body
   - attachments: [{"filename": "result.csv", "content": base64_content}]
```

#### 6.3 **Send via Resend API** (line 138)
```python
email_response = resend.Emails.send(params)
```

**This matches your Resend example:**
```python
r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "akshkhurana.tiet@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
```

**Your code adds:**
- Attachment with base64-encoded CSV file
- Dynamic recipient email from form
- Predefined subject and HTML body

#### 6.4 **Response Handling** (line 140-156)
```python
# Checks response:
- If response has 'id' attribute or 'id' key → Success
- Logs email ID for tracking
- Returns True if successful
```

#### 6.5 **Error Handling** (line 161-167)
```python
# Catches any exceptions:
- Logs error message
- Prints full traceback for debugging
- Returns False
```

### 7. **User Feedback** (Backend - line 196-199)
```python
if send_email(email, result_path):
    flash('Results sent to your email successfully!')
else:
    flash('Error sending email. Please check email configuration.')
```

### 8. **Cleanup** (Backend - line 201-202)
- Deletes uploaded original file
- Deletes result CSV file
- Both files removed from `uploads/` directory

### 9. **Page Redirect** (Backend - line 204)
- Redirects back to form page
- Flash message displayed to user

## Current Code vs Your Resend Example

### Your Example:
```python
import resend

resend.api_key = "re_9zFRXX7o_5Ge8ZUm5jwvoZYbZhL7cX1RR"

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "akshkhurana.tiet@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})
```

### Your Current Code:
```python
# API key loaded from environment variable (line 20, 24-25)
RESEND_API_KEY = os.getenv('RESEND_API_KEY')
if RESEND_API_KEY:
    resend.api_key = RESEND_API_KEY

# Email sending (line 125-138)
params = {
    "from": RESEND_FROM_EMAIL,  # From env or default
    "to": receiver_email,        # From form input
    "subject": "TOPSIS Analysis Results",
    "html": "<p>Please find attached your TOPSIS analysis results.</p>",
    "attachments": [             # Added attachment support
        {
            "filename": "result.csv",
            "content": file_content_b64  # Base64 encoded CSV
        }
    ]
}
email_response = resend.Emails.send(params)
```

## Key Differences & Improvements

1. **Environment Variables**: Your code uses env vars (better for production)
2. **Attachments**: Your code includes CSV file attachment
3. **Error Handling**: Your code has comprehensive error handling
4. **Response Validation**: Your code checks for email ID in response
5. **Dynamic Content**: Recipient email comes from form input

## Potential Issues to Check

### 1. **API Key Not Set**
- Check Railway environment variables
- Ensure `RESEND_API_KEY` is set
- Check logs for: "RESEND_API_KEY environment variable is not configured"

### 2. **Email Not Sending**
- Check Railway logs for error messages
- Verify API key is correct (starts with `re_`)
- Check Resend dashboard: https://resend.com/emails
- Verify `RESEND_FROM_EMAIL` is set (defaults to `onboarding@resend.dev`)

### 3. **Attachment Issues**
- Check file size (Resend limit: ~40MB)
- Verify base64 encoding is working
- Check logs for attachment-related errors

### 4. **Response Handling**
- Response might be dict `{"id": "..."}` or object with `.id` attribute
- Code handles both cases
- Check logs for "Email sent successfully" message

## Testing Checklist

- [ ] `RESEND_API_KEY` is set in Railway
- [ ] `RESEND_FROM_EMAIL` is set (or using default)
- [ ] Form submission works
- [ ] TOPSIS analysis completes
- [ ] Email sends successfully
- [ ] Check Railway logs for any errors
- [ ] Check Resend dashboard for sent emails
- [ ] Verify email received in inbox (check spam folder)

## Debugging Tips

1. **Check Railway Logs:**
   - Go to Railway Dashboard → Your Project → Deployments → View Logs
   - Look for print statements from `send_email()` function

2. **Test Resend API Directly:**
   - Use your example code in a test script
   - Verify API key works

3. **Check Environment Variables:**
   - Railway Dashboard → Variables tab
   - Ensure `RESEND_API_KEY` and `RESEND_FROM_EMAIL` are set

4. **Verify Email Delivery:**
   - Check Resend dashboard: https://resend.com/emails
   - See if emails are being sent
   - Check delivery status
