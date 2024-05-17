import flet as ft
from appbar import appbar
from chat_vox.config import config, get_speakers_list, write_config


class SettingsView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page

        controls = [
            appbar,
            ft.Text("一般", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.Dropdown(
                label="スピーカー",
                options=[ft.dropdown.Option(i) for i in get_speakers_list()],
                value=config["General"]["speaker"],
                on_change=lambda e: self.changed("speaker", e),
            ),
            ft.Text("わんコメ5 API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="ベースURL",
                value=config["onecomme"]["api_base_url"],
                on_change=lambda e: self.changed("onecomme_api_base_url", e),
            ),
            ft.Text("Gemini API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="APIキー",
                value=config["genai"]["api_key"],
                on_change=lambda e: self.changed("genai_api_key", e),
            ),
            ft.Text("Style Bert VITS2 API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="ベースURL",
                value=config["stylebertvits"]["api_base_url"],
                on_change=lambda e: self.changed("stylebertvits_api_base_url", e),
            ),
        ]
        super().__init__("/settings", controls)

    def changed(self, key, e):
        value = e.control.value
        match key:
            case "speaker":
                config["General"]["speaker"] = value
            case "onecomme_api_base_url":
                config["onecomme"]["api_base_url"] = value
            case "genai_api_key":
                config["genai"]["api_key"] = value
            case "stylebertvits_api_base_url":
                config["stylebertvits"]["api_base_url"] = value
        write_config()
