import os
from apiswymmer.config import BASE_DIR


def create_file(location: str) -> bool:
    try:
        os.makedirs(os.path.dirname(location), exist_ok=True)
        with open(location, "w") as f:
            f.write("")
        return True
    except Exception as e:
        rich_print(e)
        return False


def write_html(html_string: str = "", target_location: str = "index.html"):
    """Write the HTML string to the output directory."""
    create_file(BASE_DIR / "build" / target_location)
    with open(BASE_DIR / "build" / target_location, "w") as f:
        f.write(html_string)
