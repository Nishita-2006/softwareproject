# ============================================================
# CHANGES TO MAKE IN YOUR app.py
# Replace the existing config block (around line 125-133) with this:
# ============================================================

app = Flask(__name__)

# Secret key (set this as an env variable on Render)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# Flask-Mail Config — use environment variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME", "genztraumaanalyzer@gmail.com")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD", "")
app.config['MAIL_DEFAULT_SENDER'] = ('GenZTrauma Analyser', os.environ.get("MAIL_USERNAME", "genztraumaanalyzer@gmail.com"))

mail = Mail(app)


# ============================================================
# Also replace the bottom of app.py (the app.run line) with this:
# ============================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
