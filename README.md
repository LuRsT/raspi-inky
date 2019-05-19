# raspi-inky

Scripts to run on a raspberry pi with the Inky wHAT screen

## How to use

```
python paint.py --what news
```

The option "news" will scrape reuters and displays the top 10 news on the screen.

I have it on a cronjob so it runs every hour.

Like this (remember, it needs to be run by root (for now)):

```
0 * * * * python /path/to/script/paint.py --what news
```
