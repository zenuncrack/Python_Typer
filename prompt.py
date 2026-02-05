import typer 

def main():
    what_do_you_want = typer.prompt("What do you want to do?")
    typer.secho(f"You want to {what_do_you_want}", fg = typer.colors.GREEN)

    de_you_want_to_continue = typer.confirm("Do you want to continue?")
    if de_you_want_to_continue:
        typer.secho("You chose to continue", fg = typer.colors.GREEN)
    else:
        typer.secho("You chose not to continue", fg = typer.colors.RED)

if __name__ == "__main__":
    typer.run(main)