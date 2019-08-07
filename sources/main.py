import click
from reader import IO
from address import DiskHeader, DiskHeaderInformation, Apploader
from gameCode import transformGameCode
from makerCode import transformMakerCode


def decodeChunk(info, chunk):
    if info["decode"] == "hex":
        return chunk.hex().upper()
    else:
        return chunk.decode(info["decode"])


def transformChunk(info, chunk):
    if info["name"] == "Game Code":
        return transformGameCode(chunk)
    elif info["name"] == "Maker Code":
        return transformMakerCode(chunk)
    else:
        return chunk


def displayChunk(info, chunk):
    if type(chunk) == dict:
        for attr, value in chunk.items():
            print(attr, ": ", value)
    else:
        print(info["name"], ": ", chunk)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    io = IO(filename)

    for info in DiskHeader["information"]:
        chunk = io.readChunk(info["start"], info["size"])

        chunk = decodeChunk(info, chunk)
        chunk = transformChunk(info, chunk)
        displayChunk(info, chunk)

    for info in DiskHeaderInformation["information"]:
        chunk = io.readChunk(info["start"], info["size"])

        chunk = decodeChunk(info, chunk)
        chunk = transformChunk(info, chunk)
        displayChunk(info, chunk)

    for info in Apploader["information"]:
        chunk = io.readChunk(info["start"], info["size"])

        chunk = decodeChunk(info, chunk)
        chunk = transformChunk(info, chunk)
        displayChunk(info, chunk)


if __name__ == '__main__':
    main()