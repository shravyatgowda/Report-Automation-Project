import keyring as kr
user='user@example.com'
EMAIL_USER = user
email_password =kr.get_password("gmail",EMAIL_USER)
