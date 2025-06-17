import datetime

import typer

from zm10 import mathtools

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
    """素数判定"""
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i ==0:
            return False
        i += 1
    typer.echo(True)

