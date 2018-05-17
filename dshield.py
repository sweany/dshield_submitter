#!/usr/bin/env python

# https://dshield.org/specs.html

import os
import sys
import datetime
import re
import gzip
import smtplib
from email.mime.text import MIMEText

# Your return address.
sender = 'dshield@cgi-this.com'

# Send the reports here.
# Change this to your own address to validate your output if necessary.
rcpt = 'reports@dshield.org'

# Put your dshield userid number here.
dshield_userid = '0'

try:
    sys.argv[8]
except:
    print("Not enough arguments")
    sys.exit(0)

dt = datetime.datetime.utcnow()
ts = dt.strftime("%Y-%m-%dT%H:%M:%S%z")

f_log = open('/tmp/dshield.log', 'w')
#f_log.write(ts + " " + sys.argv[8] + "\n")


f_data = gzip.open(sys.argv[8], mode='rb')
# skip over the header line
f_data.readline()
for line in f_data:
    line = re.sub('["]', '', line)
    line = re.sub(',,', '\t', line)
    line = re.sub(',', '', line)
    f_log.write(line)

f_data.close()
f_log.close()


with open('/tmp/dshield.log', 'r') as fp:
    msg = MIMEText(fp.read())

msg['Subject'] = 'FORMAT DSHIELD USERID ' + dshield_userid + ' TZ +00:00'
msg['From'] = sender
msg['To'] = rcpt
s = smtplib.SMTP('localhost')
s.sendmail(sender, [rcpt], msg.as_string())
s.quit()

os.remove('/tmp/dshield.log')

