import os
from typing import Any, Dict
from apiswymmer.config import BASE_DIR, TEMPLATE_ENV, TEMPLATE_MAPPING
from rich import print as rich_print


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


def process_context(template_location: str, content: Dict[str, Any]) -> str:
    """Process the context for the template."""
    rich_print("process_context() invoked!")
    return TEMPLATE_ENV.render(location=template_location, context={"data": content})


def parse_path(path_data):
    rich_print("parse_path() invoked!")
    template = ""
    if "get" in path_data.keys():
        template = (
            TEMPLATE_MAPPING["archetypes"]
            .get("get", TEMPLATE_MAPPING["archetypes"]["_default"])
            .get("template")
        )
    if "post" in path_data.keys():
        template = (
            TEMPLATE_MAPPING["archetypes"]
            .get("post", TEMPLATE_MAPPING["archetypes"]["_default"])
            .get("template")
        )
    if "delete" in path_data.keys():
        template = (
            TEMPLATE_MAPPING["archetypes"]
            .get("delete", TEMPLATE_MAPPING["archetypes"]["_default"])
            .get("template")
        )
    if "patch" in path_data.keys():
        template = (
            TEMPLATE_MAPPING["archetypes"]
            .get("patch", TEMPLATE_MAPPING["archetypes"]["_default"])
            .get("template")
        )
    if "put" in path_data.keys():
        template = (
            TEMPLATE_MAPPING["archetypes"]
            .get("put", TEMPLATE_MAPPING["archetypes"]["_default"])
            .get("template")
        )

    content = process_context(template, path_data)
    return content


def parse_paths(path_data: Dict[str, Any]):
    rich_print("parse_paths() invoked!")
    paths = [{"path": key} | item for key, item in path_data.items()]
    parsed_content = [parse_path(path) for path in paths]

    return parsed_content


def get_templated_html(data) -> list[str]:
    """Get the templated HTML from the context."""
    rich_print("get_templated_html() invoked!")
    rich_print(data["paths"])
    return parse_paths(data["paths"])
