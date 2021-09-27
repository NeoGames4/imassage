# imassage
imassage (image + message [I know, it's very creative]) is a python app that hides text strings in image codes.
It's actually not that spectacular, but it was quite fun for a little late afternoon project.

## What it does in detail
File formats like *.png are all ending with the same string. This string indicates that the reader does not need to continue reading. So basically you can put everything behind it and the reader would not care. So all the app does is copying the original file and appending the given string. Of course there is also a feature for receiving this string from an already encrypted file, instead of appending it.

## The formats it currently supports
Currently it is only supporting *.jpg, *.jpeg and *.png files.

## How to run it
1. Download it
2. Run it via terminal for example (with `python3.7 imassages.py`)
3. Select a destination (encode, decode or exit)

When encoding:
1. Enter the file path of the original image
2. Enter the message you want to hide
3. Enter an encryption code or just press enter (!)
-> A new image-file will be created with the same image (but with the encrypted message inside)

When decoding:
1. Enter the file path of the image you want to decode
2. Enter the encryption code or just press enter, if no code is needed (!)
-> It responds with the hidden message

**(!) Warning:** Encryption is not supported yet (so even though it asks for an encryption code, it doesn't encrypt it).

## What it may be able to in the future
- *.gif-support
- *.svg-support
- *.pdf-support
- String encryption (with multiple algorithms)
- Support of some other file formats (maybe even non-image files)
Not sure when or if I'll update it.
