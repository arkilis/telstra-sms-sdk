from telstra_sms_sdk.sms import TelstraSMS

ts = TelstraSMS(client_id="8jLRC3amAJB04BflGRZYbaKmxXPaEYnY", client_secret="mejgOGM19t7WYGyP")
ts.get_token()
ts.send_sms("0425119886", sms_text="Hi this is sms test")
