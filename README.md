# telstra-sms-sdk

 A fully tested Python SDK allow you to send sms in a more easy way! 

`Current version:` 0.0.4


If you have any questions or issue, please create an issue or pull request.

--- 
### Prerequisite 



----
### To install

__Method 1: Use `pip`__
```bash
pip install telstra-sms-sdk
```

Highly recommend you to use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create your (`any`) python project.

__Method 2: Manually Install__

https://pypi.python.org/pypi/telstra-sms-sdk

----
### To use
```python
from telstra-sms-sdk.sms import TelstraSMS

ts = TelstraSMS(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
ts.get_token()
ts.send_sms("0400000000", sms_text="Hi this is unit test")
```

----
### License
MIT 

----
### Contact
- Email：<arkilis@gmail.com>

