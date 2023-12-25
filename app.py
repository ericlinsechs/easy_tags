from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import tags

import os


class EasyTagsApp(App):
    file_name = StringProperty("")
    file_path = ""
    new_tag = ""

    def build(self):
        # Load the UI layout defined in the app.kv file
        self.root = Builder.load_file("app.kv")
        return self.root

    def file_chooser_path(self):
        # Set the default path for the file chooser
        return os.path.expanduser("~")

    def on_selection(self, selection):
        # Callback function triggered when a file is selected in the file chooser
        selection = self.root.ids.file_chooser.selection
        if selection:
            file_path = selection[0]
            self.file_name = os.path.basename(file_path)
            self.file_path = file_path
            self.list_tags()

    def list_tags(self):
        # Update the UI with the list of tags for the selected file
        switch_container = self.root.ids.switch_container
        switch_container.clear_widgets()

        # Get all tags usage
        all_tags = tags.get_tags_all()
        file_tags = tags.get_tags_file(self.file_path)
        if all_tags:
            for tag in all_tags:
                is_tag_selected = tag in file_tags
                s = Switch(active=is_tag_selected)
                s.bind(
                    active=lambda instance, value, tag=tag: self.switch_callback(
                        instance, value, tag
                    )
                )
                switch_container.add_widget(
                    Label(
                        text=tag,
                        halign="right",
                        font_name="./fonts/DroidSansFallback.ttf",
                    )
                )
                switch_container.add_widget(s)
        else:
            self.show_error_popup("Error: Unable to retrieve tags")

    def input_tag(self, textinput):
        # Callback function triggered when a new tag is entered
        self.new_tag = textinput.text
        if not self.new_tag:
            self.show_error_popup("Error: Missing tag name!")
            return
        if not self.file_path:
            self.show_error_popup("Error: No selected file!")
            return
        textinput.text = ""
        # Display a popup indicating that the input is being processed
        self.popup = self.show_processing_popup("Processing......", self.create_tag)
        return

    def create_tag(self, instance):
        # Callback function triggered when a new tag is created
        new_tag = self.new_tag
        tags.add_tag(new_tag, self.file_path)
        tags.check_update(new_tag, self.file_path)
        self.list_tags()
        self.popup.dismiss()
        return

    def switch_callback(self, instance, value, tag):
        # Callback function triggered when a switch is toggled
        if value:
            tags.add_tag(tag, self.file_path)
        else:
            tags.remove_tag(tag, self.file_path)

    def show_processing_popup(self, text, callback):
        # Display a processing popup with a given message
        popup = Popup(
            title="Warning",
            content=Label(text=str(text)),
            auto_dismiss=False,
            size_hint=(None, None),
            size=(400, 200),
        )
        popup.bind(on_open=callback)
        popup.open()
        return popup

    def show_error_popup(self, text):
        # Display an error popup with a given message
        error_popup = Popup(
            title="Error",
            content=Label(text=str(text)),
            size_hint=(None, None),
            size=(400, 200),
        )
        error_popup.open()


# Run the application
if __name__ == "__main__":
    EasyTagsApp().run()
