from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = '5i0ELWTmH0LmfhyYB52VkixmgAbSFKuibtlQiRuRbnpM'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/4f5bffc3-cd89-4d50-b2c1-959b6a3ad660'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open('text.txt', 'r') as file:
    text = file.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)


with open('./speech.mp3', 'wb') as audio_file:
    result = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(result.content)
