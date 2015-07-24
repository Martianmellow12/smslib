#SMS Library
#Written By Michael Kersting Jr.
#Copyright 2015
import os
import smtplib
import imaplib
import socket
import email

carrier_emails = {
    'verizon':['vtext.com', 'vzwpix.com'],
    'alltel':['message.alltel.com', 'text.wireless.alltel.com', 'mms.alltel.net'],
    'at&t':['txt.att.net', 'mms.att.net'],
    'boost_mobile':['myboostmobile.com'],
    'sprint':['messaging.sprintpcs.com', 'pm.sprint.com'],
    't_mobile':['tmomail.net'],
    'us_cellular':['email.uscc.net', 'mms.uscc.net'],
    'virgin_mobile':['vmobl.com', 'vmpix.com']
}

verizon = ['verizon']
alltel = ['alltel', 'alltell', 'altel', 'altell']
att = ['at&t', 'atandt', 'att']
boost_mobile = ['boostmobile', 'boost', 'bmobile']
sprint = ['sprint']
t_mobile = ['tmobile']
us_cellular = ['uscellular', 'uscell']
virgin_mobile = ['virginmobile', 'virgin', 'vmobile']
#
#
#
#
#
#Messenger Class
class messenger(object):

    def make_recv_list(self, recv_data):
        final = []
        s = recv_data[0]
        for i in s:
            if not i == ' ':
                final.append(i)
        return final

    def fix_carrier(self, carrier):
        carrier = carrier.lower().replace(' ','')
        if carrier in verizon:
            return 'verizon'
        elif carrier in alltel:
            return 'alltel'
        elif carrier in att:
            return 'at&t'
        elif carrier in boost_mobile:
            return 'boost_mobile'
        elif carrier in sprint:
            return 'sprint'
        elif carrier in t_mobile:
            return 't_mobile'
        elif carrier in us_cellular:
            return 'us_celllar'
        elif carrier in virgin_mobile:
            return 'virgin_mobile'
        else:
            return None

    def send(self, phone_number, carrier, message):
        carrier = self.fix_carrier(carrier)
        if carrier == None:
            raise Exception('Invalid carrier')
        message = 'To:'+phone_number+'@'+carrier_emails[carrier][0]+'\nFrom:'+self.email+'\n'+message
        client = smtplib.SMTP('smtp.aol.com')
        client.login(self.email, self._pass)
        try:
            client.sendmail(self.email, phone_number+'@'+carrier_emails[carrier][0], message)
        except:
            raise Exception('Failed to send email')
        return

    def recvfrom(self, phone_number, carrier):
        message_type = 'sms'

        carrier = self.fix_carrier(carrier)
        if carrier == None:
            raise Exception('Invalid carrier')
        client = imaplib.IMAP4_SSL('imap.aol.com')
        client.login(self.email, self._pass)
        client.select()
        for i in carrier_emails[carrier]:
            code, results = client.search(None, '(FROM "'+phone_number+'@'+i+'")')
            if not results == ['']:
                break
        if results == ['']:
            return None
        results = self.make_recv_list(results)
        code, message = client.fetch(results[0], '(RFC822)')
        body = message[0][1]
        mail = email.message_from_string(body)
        for i in mail.walk():
            disp = str(i.get('Content-Disposition'))
            if 'attachment' in disp:
                message_type = 'mms'

        client.store(results[0], '+FLAGS', '(\\Deleted)')
        client.close()
        if message_type == 'sms':
            message = i.get_payload()
            return str(message.rstrip())
        if message_type == 'mms':
            message = i.get_payload(decode=True)
            return message

    def __init__(self, email, email_pass):
        self.email = email
        self._pass = email_pass

        if not self.email[-8:] == '@aol.com':
            raise Exception('Email address must be hosted by AOL')
        try:
            c = smtplib.SMTP('smtp.aol.com')
            resp = c.login(self.email, self._pass)
        except socket.gaierror:
            raise Exception('Not connected to the internet')
        except smtplib.SMTPAuthenticationError:
            raise Exception('Invalid credentials')
