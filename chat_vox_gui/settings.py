import flet as ft
from appbar import appbar
from chat_vox import Config, get_speakers_list


class SettingsView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page

        self.config = Config("config.ini")
        self.config.read_config()

        controls = [
            appbar,
            ft.Text("一般", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.Dropdown(
                label="スピーカー",
                options=[ft.dropdown.Option(i) for i in get_speakers_list()],
                value=self.config.config["General"]["speaker"],
                on_change=lambda e: self.changed("speaker", e),
            ),
            ft.Text("わんコメ5 API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="OneComme.exeへのパス",
                value=self.config.config["onecomme"]["path"],
                on_change=lambda e: self.changed("onecomme_path", e),
            ),
            ft.TextField(
                label="ベースURL",
                value=self.config.config["onecomme"]["api_base_url"],
                on_change=lambda e: self.changed("onecomme_api_base_url", e),
            ),
            ft.Text("Gemini API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="APIキー",
                value=self.config.config["genai"]["api_key"],
                on_change=lambda e: self.changed("genai_api_key", e),
            ),
            ft.Text("Style Bert VITS2 API", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
            ft.TextField(
                label="StyleBertVitsディレクトリへのパス",
                value=self.config.config["stylebertvits"]["path"],
                on_change=lambda e: self.changed("stylebertvits_path", e),
            ),
            ft.TextField(
                label="ベースURL",
                value=self.config.config["stylebertvits"]["api_base_url"],
                on_change=lambda e: self.changed("stylebertvits_api_base_url", e),
            ),
        ]
        super().__init__("/settings", controls)

    def changed(self, key, e):
        value = e.control.value
        match key:
            case "speaker":
                self.config.config["General"]["speaker"] = value
            case "onecomme_path":
                self.config.config["onecomme"]["path"] = value
            case "onecomme_api_base_url":
                self.config.config["onecomme"]["api_base_url"] = value
            case "genai_api_key":
                self.config.config["genai"]["api_key"] = value
            case "stylebertvits_path":
                self.config.config["stylebertvits"]["path"] = value
            case "stylebertvits_api_base_url":
                self.config.config["stylebertvits"]["api_base_url"] = value
        self.config.write_config()
