voices = [
    {"name": "Alex", "lang": "en"},
    {"name": "Luciana", "lang": "pt"},
    {"name": "Juan", "lang": "es"},
]


def getVoice(lang, defaultVoice="Alex"):
    for voiceType in voices:
        if voiceType["lang"] == lang:
            return voiceType["name"]
    return defaultVoice
