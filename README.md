# Reddit JSON Proxy

A simple proxy that fetches Reddit posts as JSON.

## Usage

Once deployed, make requests like:

```
https://your-app-url.onrender.com/fetch?url=https://www.reddit.com/r/AZURE/comments/1g0mkwi/title_unexpected_50k_azure_bill_for_openai
```

The proxy will:
1. Take your Reddit URL
2. Append `.json` to it
3. Fetch and return the JSON content

## Deploy to Render (Recommended - Free)

1. Push this folder to a GitHub repo
2. Go to [render.com](https://render.com) and sign up (no credit card needed)
3. Click **New** → **Web Service**
4. Connect your GitHub repo
5. Render auto-detects Python. Verify these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (from Procfile)
6. Click **Deploy**
7. Your proxy will be live at `https://your-app-name.onrender.com`

### Add a Custom Domain (Optional)
1. In your Render dashboard, go to your service → **Settings**
2. Scroll to **Custom Domains** → Add your domain
3. Update your DNS with the provided CNAME record
4. Free SSL is automatic

## Local Testing

```bash
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000/fetch?url=YOUR_REDDIT_URL`

## Other Deployment Options

### Railway
1. Go to [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Railway auto-detects and deploys

### Fly.io
```bash
curl -L https://fly.io/install.sh | sh
fly launch
fly deploy
```
