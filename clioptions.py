import typer 

def main(a:str = typer.Option('Daniel', help ='This is the last name of the user')):
    typer.echo(f"The name of the user is: {a}")

if __name__ == "__main__":
    typer.run(main)