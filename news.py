#!/usr/bin/env python

import datetime

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from inky import InkyWHAT
from reuters import grab_ten_news


def paint():
    print("""Inky wHAT: News from Reuters""")

    # Config for display
    inky_display = InkyWHAT("red")
    scale_size = 2.20
    padding = 15

    inky_display.set_border(inky_display.RED)

    font = ImageFont.truetype(SourceSerifProSemibold, int(10 * scale_size))
    small_font = ImageFont.truetype(SourceSerifProSemibold, int(6 * scale_size))

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    drawer = ImageDraw.Draw(img)

    trim_string = lambda s: s.strip()
    news = ' | '.join(map(trim_string, grab_ten_news()))

    print_title(drawer, inky_display, font)

    index = 0
    lenght = 60
    height = 35
    for i in range(13):
        string = news[index:lenght + index]
        drawer.text((10, height), string, inky_display.BLACK, font=small_font)
        height += 18
        index += lenght

    inky_display.set_image(img)
    inky_display.show()


def print_title(drawer, inky_display, font):
    now = datetime.datetime.now()
    title = "Updated at: {}".format(now.strftime("%Y-%m-%d %Hh"))
    drawer.text((10, 5), title, inky_display.RED, font=font)
