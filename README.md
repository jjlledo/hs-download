# hs-download

Python script to download anime episodes from HorribleSubs. You supply the show's full URL and all the episodes are added to your torrent client in ascending order.

The script currently assumes the following things:
* You are using a Mac
* You want 1080p episodes
* You are using Bittorrent as a client
* You have downloaded and installed all the dependencies in the right spots

## Dependencies

* [Python 3.6](https://www.python.org/downloads/release/python-360/)
  * [PyAutoGUI 1.0.0](https://pyautogui.readthedocs.io/en/latest/install.html)
  * [Selenium 2](http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)
* [ChromeDriver 2.27](https://chromedriver.storage.googleapis.com/index.html?path=2.27/)

## Usage

Currently you just have to use:

``` bash
$ python3 HSDownload.py
```

The script will prompt you for a URL and report the number of 1080p magnets found:
``` shell
Paste url of show to download:
http://horriblesubs.info/shows/3-gatsu-no-lion
Number of 1080p magnets found: 12
```

Since the script relies on `pyautogui` pressing enter to automate adding torrents to your client

## Motivation

We all know the feeling when you finally find a show you want to binge and go download all the episodes. In my case, when I try downloading an anime from HorribleSubs and it hasn't finished airing, I have to manually go through all the (1080p, duh) links and click on the magnets in order to do so, so I set out to automate this process using Python.
