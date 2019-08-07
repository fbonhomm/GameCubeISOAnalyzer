
MakerCode = {
    "01": "Nintendo",
    "08": "Capcom",
    "41": "Ubisoft",
    "4F": "Eidos",
    "51": "Acclaim",
    "52": "Activision",
    "5D": "Midway",
    "5G": "Hudson",
    "64": "Lucas Arts",
    "69": "Electronic Arts",
    "6S": "TDK Mediactive",
    "8P": "Sega",
    "A4": "Mirage Studios",
    "AF": "Namco",
    "B2": "Bandai",
    "DA": "Tomy",
    "EM": "Konami",
}


def transformMakerCode(chunk):
    return chunk + ' ' + (MakerCode[chunk] if chunk in MakerCode else "Unknown")
