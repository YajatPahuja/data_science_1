# TOPSIS Web Service

A Flask web application for TOPSIS multi-criteria decision analysis that sends results via email using Resend API.

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with:
```env
RESEND_API_KEY=re_your_api_key_here
RESEND_FROM_EMAIL=your_verified_email@yourdomain.com
SECRET_KEY=your_secret_key_here
```

**Note:** 
- Get your Resend API key from https://resend.com/api-keys
- For `RESEND_FROM_EMAIL`, use a verified domain email or `onboarding@resend.dev` for testing
- Verify your domain in Resend dashboard: https://resend.com/domains

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

## Railway Deployment

### Prerequisites
- Railway account (https://railway.app)
- Resend account (https://resend.com) with API key
- GitHub repository with your code

### Deployment Steps

1. **Connect Railway to your GitHub repository**
   - Go to Railway dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Configure Environment Variables in Railway**
   - Go to your project settings → "Variables" tab
   - Add the following environment variables:
     - `RESEND_API_KEY`: Your Resend API key (starts with `re_`)
     - `RESEND_FROM_EMAIL`: Your verified email address (e.g., `noreply@yourdomain.com` or use `onboarding@resend.dev` for testing)
     - `SECRET_KEY`: A random secret key for Flask sessions (optional, has default)

3. **Get Resend API Key**
   - Sign up at https://resend.com
   - Go to https://resend.com/api-keys
   - Create a new API key
   - Copy the key (starts with `re_`)

4. **Verify Domain (Optional but Recommended)**
   - For production, verify your domain: https://resend.com/domains
   - Add DNS records as instructed
   - Use your verified email as `RESEND_FROM_EMAIL`

5. **Deploy**
   - Railway will automatically deploy when you push to your main branch
   - Check the "Deployments" tab for build logs

### Email Troubleshooting on Railway

If emails are not being sent:

1. **Verify Environment Variables**
   - Check Railway project → Variables
   - Ensure `RESEND_API_KEY` is set correctly (starts with `re_`)
   - Ensure `RESEND_FROM_EMAIL` is set

2. **Check Railway Logs**
   - Go to Railway dashboard → Your project → Deployments → View logs
   - Look for error messages like:
     - "RESEND_API_KEY environment variable is not configured"
     - "Resend API error: ..."

3. **Verify Resend Account**
   - Check Resend dashboard: https://resend.com/emails
   - Verify your API key is active
   - Check if you've hit rate limits (free tier: 100 emails/day)

4. **Test Email Configuration**
   - Use `onboarding@resend.dev` as `RESEND_FROM_EMAIL` for testing
   - Verify domain if using custom email

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
