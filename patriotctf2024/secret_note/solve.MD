
It's clearly an USB data, idea was that it's a mouse movement, got nice, but wrong picture
Keyboard didn't do anything meaningful either

```
tshark -r capture.pcapng -Y usbhid.data -T fields -e usbhid.data > output.txt

```