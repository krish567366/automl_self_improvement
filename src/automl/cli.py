import click

@click.group()
def main():
    """AutoML CLI Interface"""
    pass

@main.command()
def start():
    """Launch training service"""
    print("Starting AutoML service...")

if __name__ == "__main__":
    main()