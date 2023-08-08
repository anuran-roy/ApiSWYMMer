from build import build
import sys

if __name__ == "__main__":
    try:
        source_location = sys.argv[1]
        destination_location = sys.argv[2]
        build(
            source_location=source_location,
            target_location=f'{destination_location.replace(".json", ".html")}',
        )
        sys.exit(0)
    except IndexError:
        rich_print(
            "[bold red]Please provide a file location as an argument.[/bold red]"
        )
        sys.exit(1)
