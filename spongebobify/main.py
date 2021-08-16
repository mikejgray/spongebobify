from random import choice
import typer

app = typer.Typer()


def aye_aye(text: str):
    return "".join(choice((str.upper, str.lower))(l) for l in text)


@app.callback()
def callback():
    return


@app.command()
def text(text: str = typer.Argument(..., help="The text to make sArCAstIC. If using spaces, wrap in quotes.")):
    """Make your TEXT sO sArCAstIC"""
    typer.echo(aye_aye(text))
