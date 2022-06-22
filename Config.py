import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "10916828"))
    API_HASH = os.environ.get("API_HASH", "17908e75ba2cd5838fc9eb422514d7dc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5239218621:AAFRgC8jR7YO4ixoN03YEpLH1PWe0uVG46Y")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7isg0MgjR3YX57BvUsBenEB1Jsr5I1b6G7jkMZ0p9/SrJQQdyt1dQW/+9gHAIRbv+9FNOxjWD5C991uNp15zkv/Tm8V/MsgkFCRVVN/+BRi8TeT7bUh+Ij6mUy0h3shCL1/VbKH6nMMqeTZde1RkwiAjeHgHUPsTJ1bQBrUCvIQemw9fVEF67L9AHrryIzopvxHaXD4k5+RoCYSCYgzmcCL3COTfhJ+gr1Na8j6J+zJ+4ZdggoypQWvVbuTJVyhoM5QxcKs15VSR8RjxeQA+HeMy53aXsP1R2EQPCwYouU2e0ha6CkI0VvAwWpkDoyllLlS7vqNtpsYe1USSslm4fOw==")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Y36bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
