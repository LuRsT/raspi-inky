#!/usr/bin/env python

import click


@click.command()
@click.option("--what", help="What to display")
def _paint_command(what):
    if what == "news":
        from news import paint
    try:
        paint()
    except OSError:
        print("Need to be run by root")


if __name__ == '__main__':
    _paint_command()
