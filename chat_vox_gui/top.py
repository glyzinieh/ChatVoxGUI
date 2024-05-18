import subprocess

import flet as ft
from appbar import appbar
from chat_vox import Config, ChatVox


class TopView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page

        self.config = Config("config.ini")
        self.config.read_config()

        self.start_button = ft.ElevatedButton(
            "開始", disabled=False, on_click=self.start_chat_vox
        )
        self.stop_button = ft.ElevatedButton(
            "停止", disabled=True, on_click=self.stop_chat_vox
        )

        controls = [
            appbar,
            ft.Row(
                [
                    ft.Text("わんコメ5を起動"),
                    ft.ElevatedButton(
                        "起動",
                        on_click=lambda e: self.start_app(e, "onecomme"),
                    ),
                ],
            ),
            ft.Row(
                [
                    ft.Text("Style Bert VITS2を起動"),
                    ft.ElevatedButton("起動", on_click=self.star_sbv),
                ],
            ),
            ft.Container(bgcolor=ft.colors.SURFACE_VARIANT, height=2, width="100%"),
            ft.Row(
                [
                    ft.Text("ChatVox", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                    self.start_button,
                    self.stop_button,
                ]
            ),
        ]
        super().__init__("/", controls)

    def start_app(self, e, app_name: str):
        match app_name:
            case "onecomme":
                path = self.config.config["onecomme"]["path"]
        subprocess.Popen(path, shell=True)
        e.control.disabled = True
        e.page.update()

    def star_sbv(self, e):
        path = self.config.config["stylebertvits"]["path"]
        cwd = f"{path}\\Style-Bert-VITS2"
        python_path = f"{cwd}\\venv\\Scripts\\python.exe"
        script_path = f"{cwd}\\server_fastapi.py"
        subprocess.Popen([python_path, script_path], shell=True, cwd=cwd)
        e.control.disabled = True
        e.page.update()

    def start_chat_vox(self, e):
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.page.update()

        self.chat_vox = ChatVox(
            self.config.config["onecomme"]["api_base_url"],
            self.config.config["genai"]["api_key"],
            self.config.config["stylebertvits"]["api_base_url"],
            self.config.config["General"]["speaker"],
        )
        self.chat_vox.Run()

    def stop_chat_vox(self, e):
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.page.update()

        self.chat_vox.exit_flag = True
