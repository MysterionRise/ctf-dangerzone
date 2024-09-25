Parse all QRs

Tried to decode individual and combined QR codes
Tried zsteg and other options

Correct approach to run stegseek with QR codes as passphrases, e.g.

```
docker run --rm -it -v "$(pwd):/steg" rickdejager/stegseek qr_mosaic.bmp passphrases.txt
```

Not working, so I built Docker image locally for ARM

```
docker build -t my-stegseek .
docker run --rm -it -v "$(pwd):/steg" my-stegseek qr_mosaic.bmp passphrases.txt
```

Output
```
docker run --rm -it -v "$(pwd):/steg" my-stegseek qr_mosaic.bmp passphrases.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""

[i] Original filename: "patriotCTF.bmp".
[i] Extracting to "qr_mosaic.bmp.out".
```

Okay, found 1 BMP inside, let's take a look inside

Tried zsteg

```
 zsteg patriotCTF.bmp 
imagedata           .. text: ["~" repeated 19 times]
b2,msb,bY           .. file: floppy image data (IBM SaveDskF, compressed)
b4,lsb,bY           .. text: "wUTU4B332"
b4,msb,bY           .. text: ["w" repeated 9 times]
b2,r,lsb,xY         .. text: "@@@UUUUUUUUUTTUQUTUEU]UUTUUUUTA@"
b2,r,msb,xY         .. text: "UUUUUUUUWU"
b2,g,msb,xY         .. text: "UUUuU@UUUU"
b2,b,msb,xY         .. text: "]UU[ieUUU"
b2,rgb,msb,xY       .. file: floppy image data (IBM SaveDskF, compressed)
b4,r,msb,xY         .. file: OpenPGP Public Key
b4,g,msb,xY         .. file: OpenPGP Public Key
b4,b,msb,xY         .. file: OpenPGP Public Key
b4,rgb,lsb,xY       .. text: "wUUTD3232"
b4,rgb,msb,xY       .. text: ["w" repeated 8 times]
```

Then stegseek again,

```
docker run --rm -it -v "$(pwd):/steg" my-stegseek patriotCTF.bmp passphrases.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "hD72ifj7tE83n"
[i] Original filename: "flag_qr_code.bmp".
[i] Extracting to "patriotCTF.bmp.out".
```

then you got a QR code with a flag

`PCTF{QR_M0s41c_St3g0_M4st3r}`