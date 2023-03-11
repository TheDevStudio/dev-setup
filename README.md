# Dev Setup

## Pre-requisites

* Python v3.9.x

> :information_source: **For Windows Systems**: Download Python [v3.9.x](https://www.python.org/downloads/release/python-3913/) or any suitable version from their [downloads page](https://www.python.org/downloads/)

## Setup
To setup the dev-setup folder either **clone this repo** OR run the following commands
### For Windows Systems (Run in PS)
```powershell
Invoke-WebRequest -Uri https://github.com/TheDevStudio/dev-setup/archive/master.zip -UseBasicParsing -OutFile ~\Downloads\master.zip
Expand-Archive -Path ~\Downloads\master.zip ~\Downloads
del ~\Downloads\master.zip
cd ~\Downloads\dev-setup-master 
```
### For *nix Systems
```bash
curl -LO https://github.com/TheDevStudio/dev-setup/archive/master.zip
unzip master.zip
rm master.zip
cd dev-setup-master
```

## Execute
To execute the dev setup run the following command
```
python -m setup
```



