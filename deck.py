from rich.console import RenderableType

from spiel import Deck, present

deck = Deck(name="AI assisted coding")


@deck.slide(title="Slide 1 Welcome")
def slide_1() -> RenderableType:
    return "Hello World!"


if __name__ == "__main__":
    present(__file__)