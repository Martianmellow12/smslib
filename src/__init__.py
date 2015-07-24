import smtplib
import os
import imaplib
import socket
import email
from smslib import *

'''
Copyright (c) 2014-2015 Michael W. Kersting Jr.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish and/or distribute, provided that any
redistribution, use or modification is done solely for personal benefit and
not for monetary gain, and is further subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
#
#
#
'''
This library was written to be part of the
Piabetes Framework, however I figure it may
be useful to others looking for an alternative
to SMS APIs such as Twilio and TextMagic. The
license it is released under is a modified
version of the MIT license, and allows anyone
to use the software as long as its' use is not
commercial or for other profit. Should you want
to use this library for these purposes, contact
me and I'll be happy to discuss it.
'''
