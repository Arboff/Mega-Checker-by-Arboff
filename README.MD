# Mega.nz Account Checker by Arboff.
![alt text](https://i.imgur.com/hX1cORt.png)
![alt text](https://i.imgur.com/4jA4HH3.png)


Proxyless Mega.nz account checker using the Mega.py library. All hits get storage capture and saved to a seperate txt file. Also, supports discord webhook integration.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.
## Installation on Linux
```bash
pip install colorama
pip install discord-webhook
pip install mega.py
```
## Installation on Windows
Run Mega.nz Checker by Arboff.

## Usage

Program is self explanatory. Follow on-screen instructions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


# PATCH NOTES

## 1.2

```bash
Removed bug where the program would suddenly crash at a certain account. Issue was caused by not adding "UTF-8" coding when reading the files.

ADDED:

Added CURRENT/TOTAL counter on top
Added a counter for Hits / Fails / Customs on the top of the status bar.
Added functionality to look for keyword in the account upon HIT
Added String Position in Hit message
Added TRUE/FALSE keyword flag on hits

Visual Improvements.
Recompiled .exe
```
