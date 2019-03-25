import email
import poplib
import smtplib

def get_text(msg):
	text = ""
	if msg.is_multipart():
		html = None
		for part in msg.get_payload():
			if part.get_content_charset() is None:
				charset = 'utf-8'
			else:
				charset = part.get_content_charset()
			if part.get_content_type() == 'text/plain':
				text = unicode(part.get_payload(decode=True),str(charset),"ignore").encode('utf8','replace')
			if part.get_content_type() == 'text/html':
				html = unicode(part.get_payload(decode=True),str(charset),"ignore").encode('utf8','replace')
		if html is None:
			return text.strip()
		else:
			return html.strip()
	else:
		if msg.get_content_charset() is not None:
			text = unicode(msg.get_payload(decode=True),msg.get_content_charset(),'ignore').encode('utf8','replace')
		else:
			text = unicode(msg.get_payload(decode=True),'utf8','ignore').encode('utf8','replace')
		return text.strip()

def pop_connect(email, password, server, port):
	con = poplib.POP3_SSL(server, port)
	if not email.startswith("recent:"):
		email = "recent:" + email
	con.user(email)
	con.pass_(password)
	return con

def smtp_connect(email, password, server, port):
	con = smtplib.SMTP(server, port)
	con.ehlo()
	con.starttls()
	con.ehlo
	con.login(email, password)
	return con