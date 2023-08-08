from apiswymmer.config import BASE_DIR, TEMPLATE_DIR, TEMPLATE_ENV, TEMPLATE_MAPPING
from apiswymmer.utils.utils import write_html, create_file, get_templated_html
import json
from rich import print as rich_print
import os


def build(source_location: str, target_location: str, functionality="paths") -> None:
    """Build the HTML file from the template."""
    mapping = TEMPLATE_MAPPING
    template_loc = mapping.get("archetypes", {}).get(functionality)["template"]
    rich_print(f"Template location = {template_loc}")
    html_string = TEMPLATE_ENV.render(
        location=template_loc,
        multipleContext=True,
        multipleContextKey="paths",
        context=get_templated_html(data=json.load(open(source_location, "r"))),
        # context={
        #     "paths": [
        #         """
        #         <h1 class="text-4xl">Hello, world!</h1>
        #         """,
        #         json.dumps(
        #             {
        #                 "/servertest": {
        #                     "get": {
        #                         "summary": "Sayhello",
        #                         "operationId": "sayHello_servertest_get",
        #                         "parameters": [
        #                             {
        #                                 "required": True,
        #                                 "schema": {"title": "Request"},
        #                                 "name": "request",
        #                                 "in": "query",
        #                             }
        #                         ],
        #                         "responses": {
        #                             "200": {
        #                                 "description": "Successful Response",
        #                                 "content": {"application/json": {"schema": {}}},
        #                             },
        #                             "422": {
        #                                 "description": "Validation Error",
        #                                 "content": {
        #                                     "application/json": {
        #                                         "schema": {
        #                                             "$ref": "#/components/schemas/HTTPValidationError"
        #                                         }
        #                                     }
        #                                 },
        #                             },
        #                         },
        #                     }
        #                 }
        #             },
        #             indent=4,
        #         ),
        #     ]
        # },
    )
    write_html(html_string=html_string, target_location=target_location)


if __name__ == "__main__":
    import sys

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
