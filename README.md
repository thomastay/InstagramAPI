# Instagram-API-python
Unofficial Instagram API to give you access to ALL Instagram features (like, follow, upload photo and video, etc)! Written in Python.

This is the Python port of https://github.com/mgp25/Instagram-API which is written in PHP.
It is still a work in progress to copy all of its API endpoints.

NOTE: To successfully parse for a long time you should verify your phone number in your Instagram account. 
The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page https://instagram.com/challenge

## Fork by thomastay

This is a fork of LevPasha's work that I keep updated to use as a git submodule. This allows me to add it into projects while keeping it up-to-date with changes in the Instagram API.
Any personal work of mine on the Instagram API is kept on the dev branch. 
The pip version is outdated and should not be used. 

## Installation Instructions

1. Fork/Clone/Download this repo as a submodule in your project

```
git submodule add [LINK]
```

2. Navigate to the directory

3. Install the dependencies

```
pip install -r requirements.txt
```

4. Import using the following code 
