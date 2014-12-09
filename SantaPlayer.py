__author__ = 'mhorine'

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

class SantaPlayer:

    def __init__(self, name, email, additionalExclusions=None):
        self.name = name
        self.email = email
        self.match = None
        self.exclusions = [name]
        if additionalExclusions != None:
            self.addExclusion(additionalExclusions)
        self.givingStatus = 'Needs Match'
        self.receivingStatus = 'Needs Match'
        self.msg = None

    def printInfo(self):
        print('Name: {0}\nEmail: {1}\nMatch: {2}\nExclusions: {3}\nGiving Status: {4}\nReceiving Status: {5}\n'.format(
              self.name, self.email, getName(self.match), self.exclusions, self.givingStatus, self.receivingStatus))

    def addExclusion(self, exclusion):
        if (isinstance(exclusion, list)):
            for e in exclusion:
                self.exclusions.append(e)
        else:
            self.exclusions.append(exclusion)

    def createEmailMessage(self):
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = 'Sibling Gift Exchange'
        self.msg['From'] = formataddr(('Secret Santa', 'mdlhorine@gmail.com'))
        self.msg['To'] = 'mdlhorine@gmail.com'
        self.msg['Bcc'] = 'matthew.horine@teachforall.org'

        text = """\
        Hi {0},

        Welcome to the Inaugural Sibling Gift Exchange!  You have been assigned to give a gift to {1}.  \
        The recommend spend is $30.

        Merry Christmas! See you soon!

        Secret Santa
        """.format(self.name, getName(self.match))

        html = """\
        <html>
            <head></head>
            <body>
                <p>Hi {0},</p>
                <p>Welcome to the Inaugural Sibling Gift Exchange!  You have been assigned to give a gift to {1}. \
        The recommend spend is $30.</p>
                <p>Merry Christmas! See you soon!</p>
                <p>Secret Santa</p>
            </body>
        </html>
        """.format(self.name, getName(self.match))

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        self.msg.attach(part1)
        self.msg.attach(part2)

# Helper method to get name an object reference

def getName(object):
    santaPlayer = object
    if (santaPlayer):
        return santaPlayer.name
    else:
        return 'None'