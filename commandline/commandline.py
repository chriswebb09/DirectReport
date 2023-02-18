import click

@click.command()
@click.option('--new', help='New entry')
@click.option('--list', help='Previous entries')

def interface(entry):
    """Takes in ENTRY for DirectReport"""
    click.echo(f"{entry}")

if __name__ == '__main__':
    interface()
