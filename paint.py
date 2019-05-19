#!/usr/bin/env python

import click

@click.command()
@click.option("--what", help="What to display")
def paint(what):
    if what == "news":
        from news import paint
    paint()

if __name__ == '__main__':
    paint()
