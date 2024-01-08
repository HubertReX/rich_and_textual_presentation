import inspect
from textwrap import dedent

from rich.box import SQUARE
from rich.console import RenderableType
from rich.layout import Layout
from rich.markdown import Markdown
from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style
from rich.syntax import Syntax

from spiel import Deck, Slide, present
from spiel.deck import Deck


SPIEL = "[Spiel](https://github.com/JoshKarpel/spiel)"
RICH = "[Rich](https://rich.readthedocs.io/)"

def pad_markdown(markup: str) -> RenderableType:
    return Padding(Markdown(dedent(markup), justify="center"), pad=(0, 5))

deck = Deck(name="AI assisted coding")


@deck.slide(title="Slide 1 Welcome")
def slide_1() -> RenderableType:
    return "Hello World!"


@deck.slide(title="Decks and Slides")
def code() -> RenderableType:
    markup = f"""\
        ## Decks are made of Slides

        Here's the code for `Deck` and `Slide`!

        The source code is pulled directly from the definitions via [inspect.getsource](https://docs.python.org/3/library/inspect.html#inspect.getsource).

        ({RICH} supports syntax highlighting, so {SPIEL} does too!)
        """
    root = Layout()
    upper = Layout(pad_markdown(markup), size=len(markup.split("\n")) + 1)
    lower = Layout()
    root.split_column(upper, lower)

    def make_code_panel(obj: type) -> RenderableType:
        lines, line_number = inspect.getsourcelines(obj)
        return Panel(
            Syntax(
                "".join(lines),
                lexer="python",
                line_numbers=True,
                start_line=line_number,
            ),
            box=SQUARE,
            border_style=Style(dim=True),
            height=len(lines) + 2,
        )

    lower.split_row(
        Layout(make_code_panel(Deck)),
        Layout(make_code_panel(Slide)),
    )

    return root

if __name__ == "__main__":
    present(__file__)
    
