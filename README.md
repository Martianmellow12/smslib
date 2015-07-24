<h1>SMSlib</h1>
<h3>A library that allows communication via text messages in Python</h3>
<hr>
<h3>About</h3>
<p>This library offers a cost-effective alternative to texting services APIs such as TextMagic and Twilio. By using
SMS-to-Email and Email-to-SMS services often offerd by carriers, a user can text an email address, and have this
read and managed by a Python script, and the Python script can respond. Currently, there are 8 supported carriers,
though I plan to add more as requests come in. These carriers are:</p>
<ul>
  <li>Verizon</li>
  <li>Alltel</li>
  <li>AT&T</li>
  <li>Boost Mobile</li>
  <li>Sprint</li>
  <li>T Mobile</li>
  <li>US Cellular</li>
  <li>Virgin Mobile</li>
</ul>
<hr>
<h3>Usage</h3>
<p>SMSlib is very easy to use. At the moment, only email addresses hosted by AOL will work, though I plan to add support 
for others later. To start, we need to create a <code>messenger</code> like in the next example:</p>
<code>import smslib</code><br>
<code>client = smslib.messenger('youremail@aol.com', 'yourpassword')</code>
<p>Lets begin by sending a message to (555) 123-4567:</p>
<code>client.send("5551234567", "yourcarrier", "Hello World!")</code>
<p>Receiving a text is very similar:</p>
<code>client.recvfrom("5551234567", "yourcarrier")</code>
<p>This will return the oldest message sent by the number, or <code>None</code> if no messages are found.</p>
