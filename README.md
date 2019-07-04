# Text_Bot

This is a text bot to send messages to phone numbers without Twilio or any other
external libraries.

To run, modify config.py. Then,
```
python3 text_bot.py
```

Use this site to figure out the MMS Gateway address of the number you want to
text: https://freecarrierlookup.com/.

Make sure you Turn On Allowing Secure apps: https://myaccount.google.com/lesssecureapps.

## Todo
* Automatically implement MMS Gateway based on address.
* Add infrastructure to send text messages periodically
