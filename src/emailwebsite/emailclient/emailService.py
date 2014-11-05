from __future__ import unicode_literals
import smtplib
import imaplib
import base64
import email
from email.header import decode_header
from imapclient import IMAPClient
import quopri
import io

def sendMail(user, token, to, subject, message):
	auth_string = 'user=%s\1auth=Bearer %s\1\1' % (user, token)
	auth_string = base64.b64encode(bytes(auth_string, 'ascii')).decode('ascii')

	smtpserver = smtplib.SMTP('smtp.gmail.com',587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.docmd('AUTH', 'XOAUTH2 ' + auth_string)
	header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:'+subject+' \n'
	msg = header + '\n' + message + '\n\n'
	smtpserver.sendmail(user, to, msg)
	smtpserver.close()

def getMail(user, token):
	imap_conn = IMAPClient('imap.gmail.com', use_uid=True, ssl=True)
	imap_conn.oauth2_login(user, token)

	select_info = imap_conn.select_folder('INBOX')
	#print('%d messages in INBOX' % select_info['EXISTS'])

	messages = imap_conn.search(['NOT DELETED'])
	#print("%d messages that aren't deleted" % len(messages))

	#print()
	#print("Messages:")
	response = imap_conn.fetch(messages, ['RFC822', 'ENVELOPE'])
	theList = []
	for msgid, data in response.items():
		msg = email.message_from_string(data['RFC822'])
		theSubject = ""
		if msg['Subject'] is not None:
			decodefrag = decode_header(msg['Subject'])
			subj_fragments = []
			for s, enc in decodefrag:
				if enc:
					s = str(s, enc)

				if str(type(s)) == "<class 'bytes'>":
					s = s.decode('utf-8')

				theSubject += str(s)

		attachments = []
		body = None
		html = None
		for part in msg.walk():
			attachment = parse_attachment(part)
			if attachment:
				attachments.append(attachment)
			elif part.get_content_type() == 'text/plain':
				if body is None:
					body = ""
				if part.get_content_charset() is None:
					# We cannot know the character set, so return decoded "something"
					body += str(part.get_payload(decode=True).decode('ascii'))
				else:
					body += str(part.get_payload(decode = True),
							part.get_content_charset(),
							'replace')
			elif part.get_content_type() == 'text/html':
				if html is None:
					html = ""
				if part.get_content_charset() is None:
					# We cannot know the character set, so return decoded "something"
					body += str(part.get_payload(decode=True))
				else:
					html += str(part.get_payload(decode = True),
							part.get_content_charset(),
							'replace')
		theBody = body
		theHtml = html

		theEnvelope = data['ENVELOPE']
		theTime = theEnvelope[0]
		#theSubject = theEnvelope[1]
		theAdress = theEnvelope[4]
		theSender = theAdress[0]

		theObject = (theSubject, theSender, theBody, theHtml, theTime.strftime("%Y-%m-%d %H:%M:%S"))
		theList.append(theObject)
		#print(theObject)
	#print(theList)
	#return (theSubject, theSender,  theMessage, theTime.strftime("%Y-%m-%d %H:%M:%S"))
	return theList

#not own code... just to make attachments to work
def parse_attachment(message_part): 
	content_disposition = message_part.get("Content-Disposition", None) 
	if content_disposition: 
			dispositions = content_disposition.strip().split(";") 
			if bool(content_disposition and dispositions[0].lower() == "attachment"):  
				file_data = message_part.get_payload(decode=True) 
				# Used a StringIO object since PIL didn't seem to recognize 
				# images using a custom file-like object 
				attachment = io.BytesIO(file_data) 
				attachment.content_type = message_part.get_content_type() 
				attachment.size = len(file_data) 
				attachment.name = None 
				attachment.create_date = None 
				attachment.mod_date = None
				attachment.read_date = None 
				for param in dispositions[1:]: 
					name,value = param.split("=") 
					name = name.lower() 
					if name == "filename": 
						attachment.name = value 
					elif name == "create-date":
						attachment.create_date = value #TODO: datetime
					elif name == "modification-date":
						attachment.mod_date = value #TODO: datetime 
					elif name == "read-date": 
						attachment.read_date = value #TODO: datetime
				return attachment 
	return None 