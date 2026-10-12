#email validation
#regex
#email authentication
#email, ssl, smtp
#password validation
#regex
#password suggestion
#random ad arange
#password hashing
#haslib, bycrypt
#date time
#datetime
#time
#threading
#voice assistant and tts/machine translation
#goggle_translate
#edge_tts
#whisper openai
#scipy.wav


#regex

# import re

# text = "I love python"
# pattern = re.search("python", text)
# if pattern:
#     print("python found in text")
# else:
#     print("python not found")


#regex special characters
# ^ = start with
# $ = end with
# * = zero or more
# + = one or more
# ? = zero or one
# [] = choose from the following characters
# {} = exact number
# \d = digit
# \w = word character

# escape characters

# text = "Digit"
# pattern = re.search(r"[a-zA-Z]", text)
# if pattern:
#     print("text found")
# else:
#     print("text not found")


# # regex for email validation

# email = input("Enter your mail: ")
# pattern = r"^[\w\.]+@[\w\.]+.\[\w]{2,}"
# pattern = r"^[\w\.]+@[\w\.]+\.[\w]{2,}"
# pattern = r"^[\w\.]+@[\w\.]+\.\w+$"
# result = re.match(pattern, email)
# if result:
#     print("Email validation successful")
# else:
#     print("Incorrect email format")


#password validation
# import re
# import bcrypt

# password = input("Enter your password: ")
# password must have more than 8 char
# password must contain a capital letter
# password must contain special char
# password must contain num 

# if len(password) < 8:
#     print("Password must be more than 8 characters")
# elif not re.search(r"[A-Z]", password):
#     print("Password must contain a capital letter")
# elif not re.search(r"[a-z]", password):
#     print("Password must contain a small letter")
# elif not re.search(r"[!@#$%^&*]", password):
#     print("Password must contain a special chararcter")
# elif not re.search(r"[0-9]", password):
#     print("Password must contain a number")
# else:
#     print("Password is strong enough")


# pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W]).{8,}"
# if re.fullmatch(pattern, password):
#     print("Password validation successful")
#     hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#     print("Password hashing successful", hashed_password)
# else:
#     print("Weak password")

# password_login = input("Enter password: ")
# if bcrypt.checkpw(password_login.encode(), hashed_password):
#     print("Login successful")

# else:
#     print("Invalid credentials")


#email authentication
# import os
# import smtplib
# import ssl
# import random
# import string
# from email.mime.text import MIMEText

# sender_mail = "oluwalovely@gmail.com"
# sender_password = os.environ["SMTP_APP_PASSWORD"]
# receiver_mail = input("Enter mail: ")
# verification_code = ""
# for i in range(6):
#     verification_code += random.choice(string.digits)
#     # print("verification code: ", verification_code)

# message = MIMEText(f"""
#                 Welcome to SQI_LMS your verification code is {verification_code}
#                     Techpreneur awon lobaloba
#                     You thought I forgot? 
#                     """)
# message["From"] = "oluwalovely@gmail.com"
# message["To"] = "oladejotoluwanimi51@gmail.com"
# message["subject"] = "Registration verification"

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_mail, sender_password)
#     server.sendmail(sender_mail, receiver_mail, message.as_string())
# print("Mail sent successfully")



#PIPELINE

# pip install argostranslate
# pip install edge_tts
# pip install pygame
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import argostranslate.translate as tr
import asyncio
import edge_tts
import pygame
# import os

SAMPLE_RATE = 16000
DURATION = 10
AUDIO_FILE = "speech.wav"
VOICE_FILE = "voice.mp3"

print("Loading whisper model")

Languages = {
    "1" : {
        "name": "French",
        "code": "fr",
        "voice": "fr-FR-DeniseNeural"
    },
    "2" : {
        "name": "Spanish",
        "code": "es",
        "voice": "es-ES-ElviraNeural"},
    "3" : {
        "name": "German",
        "code": "de",
        "voice": "de-DE-KatjaNeural"
    },
    "4" : {
        "name": "Italian",
        "code": "it",
        "voice": "it-IT-ElsaNeural"},
    "5" : {
        "name": "Yoruba",
        "code": "yo",
        "voice": "yo-NG-AminaNeural"},
    "6" : {
        "name": "Arabic",
        "code": "ar",
        "voice": "ar-SA-HamedNeural"},
    "7" : {
        "name": "Hausa",
        "code": "ha",
        "voice": "ha-Latn-NG-AminuNeural"},
}

model = whisper.load_model("base")
# print(whisper.available_models())
print("Whisper loaded successfully")
def record_audio():
    print("Speak now\n")
    data = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate = SAMPLE_RATE,
        channels = 1,
        dtype = "int16"
    )
    sd.wait()

    write(AUDIO_FILE,
          SAMPLE_RATE,
          data)

# record_audio()

def speech_to_text():
    result = model.transcribe(AUDIO_FILE)
    text = result["text"]
    language = result["language"]

    return text, language
record_audio()
text, language = speech_to_text()
print("you said ", text)
print("Language: ", language)

def translate_text(text, source_language, target_language):
    translated = tr.translate(text, source_language, target_language)
    return translated

async def text_to_speech(text, voice):
    communicate = edge_tts.Communicate(
            text = text, 
            voice = voice
    )
    await communicate.save(VOICE_FILE)

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()

while True:
    print("Select a language to translate to: ")
    for key, value in Languages.items():
        print(f"{key}. {value['name']}")

    choice = input("Enter your choice: ")

    if choice in Languages:
        target_language = Languages[choice]["code"]
        voice = Languages[choice]["voice"]
        translated_text = translate_text(text, language, target_language)
        print(f"Translated text: {translated_text}")
        asyncio.run(text_to_speech(translated_text, voice))
        play_audio(VOICE_FILE)
    else:
        print("Invalid choice. Please try again.")