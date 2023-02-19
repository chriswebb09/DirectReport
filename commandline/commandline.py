#!/usr/bin/env python3

import click

@click.command()
@click.option('--new', help='New entry')
@click.option('--list', help='Previous entries')

def interface(entry):
    """Takes in ENTRY for DirectReport"""
    click.echo(f"{entry}")
    app()

if __name__ == '__main__':
    print(__package__)
    print("Main")
    interface()
