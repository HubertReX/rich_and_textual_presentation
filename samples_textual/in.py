#!/Users/hubertnafalski/Documents/Projects/rich_and_textual_presentation/.venv/bin/python
from textual.app import App, ComposeResult
from textual.widgets import TextArea
# from textual_textarea import TextEditor

import sys

class InlineEditor(App):
    CSS = """
    TextArea {
        height: auto;
        max-height: 60vh;
        border: none;
    }
    """
    
    # def on_mount(self) -> None:
    def on_ready(self):
        
        if len(sys.argv) > 1:
            file_name = sys.argv[1]
        else:
            file_name = sys.argv[0]
            
        with open(file_name) as f:
            text = f.read()
        editor = self.query_one(TextArea)
        editor.text = text
        editor.focus()
        
    def compose(self) -> ComposeResult:
        yield TextArea(
        # yield TextEditor(
            language="python", 
            theme="vscode_dark", 
            tab_behavior="indent", 
            show_line_numbers=True
        ) # monokai vscode_dark github_light dracula css
        
if __name__ == "__main__":
    app = InlineEditor().run(inline=True)