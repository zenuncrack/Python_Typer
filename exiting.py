import typer

def main(exit_style:str = 'Normal'):
    if exit_style =='Normal':
        typer.secho('Normal exit',fg = typer.colors.GREEN)
        raise typer.Exit()
    elif exit_style == 'Error':
        typer.secho('Error exit',fg = typer.colors.RED)
        raise typer.Exit('Error')
    elif exit_style == 'Abort':
        typer.secho('Abort exit', fg = typer.colors.YELLOW)
        raise typer.Exit('Abort')
    else:
        typer.secho('Unknown exit style, performing normal exit', fg = typer.colors.BLUE)


if __name__ == "__main__":
    typer.run(main)