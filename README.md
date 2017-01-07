# telstra-sms-sdk

 A fully tested Python SDK allow you to send sms in a more easy way! 

`Current version:` 0.0.7
`Support Python version`: >=python 2.6 

If you have any questions or issue, please create an issue or pull request.



 
### Prerequisite 

Before you are using this lib, please register an App on Telstra at https://dev.telstra.com/. Their sms will be activated within a fews days. So be patient or you can just call them. :)

----
### To Install

__Method 1: Use `pip`__
```bash
pip install telstra-sms-sdk
```

Highly recommend you to use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create your (`any`) python project.

__Method 2: Manually Install__

https://pypi.python.org/pypi/telstra-sms-sdk

----
### To Use and Example
```python
from telstra_sms_sdk.sms import TelstraSMS


# CLIENT_IDi and CLIENT_SECRET are strings getting from Telstra app  

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

