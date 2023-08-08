from pathlib import Path
import sys
import yaml
from jinja2 import FileSystemLoader, Environment
from typing import Optional, Dict, List, Any
import sys
from rich import print as rich_print
import os

BASE_DIR = Path(__file__).parent.parent

if BASE_DIR not in sys.path:
    print(f"Added {BASE_DIR} to sys.path")
    sys.path.append(BASE_DIR.resolve(strict=True))

TEMPLATE_DIR = BASE_DIR / "templates" / "simple"
BUILDS_DIR = BASE_DIR / "build"


class TemplatingEnv:
    def __init__(
        self,
        follow_links: Optional[bool] = False,
        enable_async: Optional[bool] = False,
        enable_autoescape: Optional[bool] = False,
        *args: Optional[List],
        **kwargs: Optional[Dict],
    ) -> None:
        self.loader = FileSystemLoader(TEMPLATE_DIR, followlinks=follow_links)
        self.environment = Environment(
            loader=self.loader, enable_async=enable_async, autoescape=enable_autoescape
        )
        self.template_config = (
            yaml.safe_load(stream=open(TEMPLATE_DIR / "config.yml"))
            if os.path.exists(TEMPLATE_DIR / "config.yml")
            else {}
        )

    def render(
        self,
        location: str,
        context: Optional[Dict] = {},
        verbose: Optional[bool] = True,
    ) -> str:
        """
        location: Location of template to use
        context: Context dictionary to pass to template
        verbose: Whether to print debug data
        """
        if verbose:
            rich_print(f"Context dictionary = {context}")
        required_template = self.environment.get_template(location)
        return required_template.render(**context, **self.template_config)


TEMPLATE_ENV = TemplatingEnv()

TEMPLATE_MAPPING: Dict[str, Any] = {
    "archetypes": {
        "paths": {"template": "components/paths.html", "objects": []},
        "_default": {"template": "base.html", "objects": []},
    }
}
