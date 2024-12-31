"""Command-line interface."""

import click
from agentNaomi.client import setup_studio
from agentNaomi.utils import FileTypeError

@click.group()
@click.version_option()
def main() -> None:
    """
    Naomi - Command Line Interface for utilizing Agent Naomi toolkit.
    
    """
    pass

@main.command()
@click.argument("name", type=click.STRING)
def greet(name: str) -> None:
    """Greets a user by NAME."""
    click.echo(f"Hello, {name}! Welcome to Agent Naomi.")
    
@main.command()
@click.argument("file_name", type=click.STRING)
def check_data(file_name: str) -> None:
    """Quick view of your input question bank database."""
    
    if not file_name.endswith('.yaml'):
        raise FileTypeError("Can only accept yaml files.")
    
    try:
        click.echo(f"Reading from {file_name}")
        handler = DataHandler(file_name)
        click.echo(f"Data: {handler.data}")
    except Exception as e:
        click.echo(f"Error: {e}")
            
@main.command()
@click.argument("name", type=click.STRING)
@click.argument("teamspace", type=click.STRING)
@click.argument("user", type=click.STRING)
def setup(name: str, teamspace: str, user: str) -> None:
    """
    Sets up a connection to the Lightning AI Studio.

    Args:
        name (str): Name of the Lightning AI Studio.
        teamspace (str): Name of the teamspace in the studio.
        user (str): Username of the user connecting.
    """
    
    studio = setup_studio(name, teamspace, user)
    click.echo(f"Connected to {studio.name} in teamspace {studio.teamspace} as {studio.user}")
    return studio

if __name__ == "__main__":
    main(prog_name="Agent Naomi")  # pragma: no cover