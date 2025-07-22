import datetime

import typer

from zm10 import mathtools
from zm10 import demo

app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))


@app.command()
def is_prime(x):
    """
    素数の判定
    """
    typer.echo(mathtools.is_prime(x))


@app.command()
def hello(name:str ="wataru"):
    typer.echo(demo.hello(name))
