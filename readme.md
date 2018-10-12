# Sprout Video

## Description
Downloads videos from sprout using sproutvideo API calls and downloadable links.

## Getting started

### Dependencies

Project depends on gregmccoy/sproutvideo-python See: https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github

I run using virtualenvironment

```
pip install virtualenv

virtualenv myvenv
source myvenv/bin/activate

pip install git+https://github.com/gregmccoy/sproutvideo-python@master

pip install -r requirements.txt
```

You need to collect an API token from sprout. Place this in a file named ```config.ini ``` structured like:

```
[auth]
token = YOUR API TOKEN
```

## Known issues:
For some reason -- you need to delete the first header row in videos.tsv after it generates ...
Also: You need to globally enable downloading under account settings for the source of video you are downloading.
The program can be run multiple times and will skip/not re-download files that already exist in the download directory.


There are a few warning for old libraries. To ignore warnings, use the ```-W ignore``` attribute.

```
python -W ignore main.py
```
