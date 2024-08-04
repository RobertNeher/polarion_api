import flet as ft

from utilities.configuration import Configuration
from view.project import ProjectView

def main(page: ft.Page):
    config = Configuration()
    projectView = ProjectView()

    page.add(controls=[
        ft.Column(controls=[
            ft.Text(f"Projects found in server {config.schema}://{config.polarionHost}",
                    text_align = ft.TextAlign.CENTER,
                    style=config.headerStyle
            ),
            ft.GridView(controls=projectView.widgets)
        ])
    ])



ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
