import typer
from typing import Optional


def main(a:str, b:int, c:Optional[float]=3.14):
    typer.echo("Welcome to typer")
    typer.echo(f"the value of <a> is {a} and the value of <b> is {b} and the value of <c> is {c}")


if __name__ == '__main__':
    typer.run(main)