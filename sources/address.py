
DiskHeader = {
    "start": 0x00000000,
    "information": [
        {"name": "Game Code", "start": 0x0000, "size": 0x0004, "decode": "hex"},
        {"name": "Maker Code", "start": 0x0004, "size": 0x0002, "decode": "utf8"},
        {"name": "Disk ID", "start": 0x0006, "size": 0x0001, "decode": "hex"},
        {"name": "Version", "start": 0x0007, "size": 0x0001, "decode": "hex"},
        {"name": "Audio Streaming", "start": 0x0008, "size": 0x0001, "decode": "hex"},
        {"name": "Stream Buffer Size", "start": 0x0009, "size": 0x0001, "decode": "hex"},
        {"name": "DVD Magic Word (0xc2339f3d)", "start": 0x001c, "size": 0x0004, "decode": "hex"},
        {"name": "Game Name", "start": 0x0020, "size": 0x03e0, "decode": "utf8"},
        {"name": "offset of debug monitor (dh.bin)", "start": 0x0400, "size": 0x0004, "decode": "hex"},
        {"name": "address to load debug monitor", "start": 0x0404, "size": 0x0004, "decode": "hex"},
        {"name": "offset of main executable DOL (bootfile)", "start": 0x0420, "size": 0x0004, "decode": "hex"},
        {"name": "offset of the FST (fst.bin)", "start": 0x0424, "size": 0x0004, "decode": "hex"},
        {"name": "size of FST", "start": 0x0428, "size": 0x0004, "decode": "hex"},
        {"name": "maximum size of FST (usually its same as FST size)", "start": 0x042C, "size": 0x0004, "decode": "hex"},
        {"name": "user position", "start": 0x0430, "size": 0x0004, "decode": "hex"},
        {"name": "user length", "start": 0x0434, "size": 0x0004, "decode": "hex"},
    ]
}

DiskHeaderInformation = {
    "start": 0x00000440,
    "information": [
        {"name": "Debug-monitor Size", "start": 0x0440, "size": 0x0004, "decode": "hex"},
        {"name": "Simulated Memory Size", "start": 0x0444, "size": 0x0004, "decode": "hex"},
        {"name": "Argument offset", "start": 0x0448, "size": 0x0004, "decode": "hex"},
        {"name": "Debug flag", "start": 0x044c, "size": 0x0004, "decode": "hex"},
        {"name": "Track Location", "start": 0x0450, "size": 0x0004, "decode": "hex"},
        {"name": "Track size", "start": 0x0454, "size": 0x0004, "decode": "hex"},
        {"name": "Countrycode", "start": 0x0458, "size": 0x0004, "decode": "hex"},
    ]
}

Apploader = {
    "start": 0x00002440,
    "information": [
        {"name": "Date (version) of the apploader in ASCII", "start": 0x2440, "size": 0x000a, "decode": "ascii"},
        {"name": "Apploader entrypoint", "start": 0x2450, "size": 0x0004, "decode": "hex"},
        {"name": "size of the apploader (32 bit) (usually 0x2000)", "start": 0x2454, "size": 0x0004, "decode": "hex"},
    ]
}