import typer 
from typing import Optional

def main(a:str=typer.Argument(...),b:Optional[int]=typer.Argument(None)):
    typer.echo(f"The <a> is a required argument and its value is: {a}")
    typer.echo(f"The <b> is a an optional argument and its value is: {b}")

if __name__ == "__main__":
    typer.run(main)