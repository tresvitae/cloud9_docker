#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello World!')
    
if __name__ == '__name__':
    hello()