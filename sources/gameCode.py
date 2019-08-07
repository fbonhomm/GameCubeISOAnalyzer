
ConsoleId = {
    "44": " Emulated/Ported/Promotional",
    "47": " Gamecube",
    "55": " GBA-Player Boot CD",
}

CountryCode = {
    "45": " USA/NTSC",
    "4A": " Japan/NTSC",
    "50": " Europe/PAL",
    "55": " Europe/PAL (LoZ Oot (MQ))?",
}


def transformGameCode(chunk):
    return {
        "GameCode": bytes.fromhex(chunk[2:6]).decode('utf8'),
        "ConsoleId": chunk[:2] + (ConsoleId[chunk[:2]] if chunk[:2] in ConsoleId else "Unknown"),
        "CountryCode": chunk[6:] + (CountryCode[chunk[6:]] if chunk[6:] in CountryCode else "Unknown"),
    }