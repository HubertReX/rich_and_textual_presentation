# import asyncio
import pyfiglet
from textwrap import dedent
from pathlib import Path
from click import edit

from rich.box import HEAVY, SQUARE
from rich.panel import Panel
from rich.console import RenderableType
from rich.style import Style
from rich.text import Text
from rich.align import Align
from rich.markdown import Markdown
from rich.padding import Padding

from spiel import Deck, Slide, present, init_app, SuspendType
from spiel.renderables.image import Image

THIS_FILE = Path(__file__).resolve()
THIS_DIR = THIS_FILE.parent
CYBORG_DEV_IMAGE_PATH = THIS_DIR / "img" / "cyborg_dev_02.jpeg"

# https://github.com/wasi-master/gradient_figlet/blob/main/gradient_figlet/__main__.py
good_gradients = {
    "Roseanna": ["#ffafbd", "#ffc3a0"],
    "Sexy Blue": ["#2193b0", "#6dd5ed"],
    "Purple Love": ["#cc2b5e", "#753a88"],
    "Piglet": ["#ee9ca7", "#ffdde1"],
    # "Mauve": ["#42275a", "#734b6d"],
    "50 Shades of Grey": ["#bdc3c7", "#2c3e50"],
    "A Lost Memory": ["#de6262", "#ffb88c"],
    "Socialive": ["#06beb6", "#48b1bf"],
    "Cherry": ["#eb3349", "#f45c43"],
    "Pinky": ["#dd5e89", "#f7bb97"],
    "Lush": ["#56ab2f", "#a8e063"],
    "Kashmir": ["#614385", "#516395"],
    "Tranquil": ["#eecda3", "#ef629f"],
    "Pale Wood": ["#eacda3", "#d6ae7b"],
    "Green Beach": ["#02aab0", "#00cdac"],
    "Sha La La": ["#d66d75", "#e29587"],
    "Frost": ["#000428", "#004e92"],
    "Almost": ["#ddd6f3", "#faaca8"],
    "Virgin America": ["#7b4397", "#dc2430"],
    "Endless River": ["#43cea2", "#185a9d"],
    "Purple White": ["#ba5370", "#f4e2d8"],
    "Bloody Mary": ["#ff512f", "#dd2476"],
    "Can you feel the love tonight": ["#4568dc", "#b06ab3"],
    "Bourbon": ["#ec6f66", "#f3a183"],
    "Dusk": ["#ffd89b", "#19547b"],
    "Relay": ["#3a1c71", "#ffaf7b"],
    "Decent": ["#4ca1af", "#c4e0e5"],
    "Sweet Morning": ["#ff5f6d", "#ffc371"],
    "Scooter": ["#36d1dc", "#5b86e5"],
    "Celestial": ["#c33764", "#1d2671"],
    # "Royal": ["#141e30", "#243b55"],
    "Ed's Sunset Gradient": ["#ff7e5f", "#feb47b"],
    "Peach": ["#ed4264", "#ffedbc"],
    "Sea Blue": ["#2b5876", "#4e4376"],
    "Orange Coral": ["#ff9966", "#ff5e62"],
    "Aubergine": ["#aa076b", "#61045f"],
}
from colour import Color, rgb2hex

def figlet_gradient(text: str, gradient="Bloody Mary", font="roman"):
    gradient = good_gradients.get(gradient, "Bloody Mary")
    color1 = Color(gradient[0])
    color2 = Color(gradient[1])
    lines = pyfiglet.figlet_format(text, font=font).split("\n")
    gradient_colors = list(color1.range_to(color2, len(lines)))
    rich_text = [] # Text()
    for c, l in zip(gradient_colors, lines):
        # rich_text.append(l + "\n", style=c.hex_l)
        rich_text.append(f"[{c.hex_l}]{l}[/]")
    return "\n".join(rich_text)

# app = init_app(THIS_FILE)
deck = Deck(name="AI assisted coding")
# app.deck = deck

# def send_message(message: str) -> None:
#     global app
#     app.set_message_temporarily(
#         Text(
#             message,
#             style=Style(dim=True),
#         ),
#         delay=10,
#     )

def edit_this_file(suspend: SuspendType) -> None:
    # send_message("edit_this_file!")
    with suspend():
        edit(filename=THIS_FILE)

# def quit() -> None:
#     send_message("Bye!")
#     app.action_quit()

# async def first() -> None:
#     send_message("Go to first slide")
#     await app.action_first_slide()

# async def last() -> None:
#     send_message("Go to last slide")
#     await app.action_last_slide()


CUSTOM_BINDINGS = {
    "e": edit_this_file,
    # "q": quit,
    # "ESC": quit,
    # 'home': first,
    # 'up': first,
    # 'end': last,
    # 'down': last,
    }
    
CONTENT = {
    "Agenda": {
        "align": "justify",
        "text": """
## Agenda

* 1️⃣ AI tools acceptance process
* 2️⃣ GitHub Copilot live demo
* 3️⃣ __Bonus__ - full local, totally free

""",
    },
    "1. AI Image": {
        "align": "justify",
        "image_path": CYBORG_DEV_IMAGE_PATH,
    },
    "1. Acceptance process": {
        "align": "justify",
        "text": """
## Acceptance process

* New Application or Changes to Application (NAA) - on hold     🔴
* Business Case                                   - in progress ⏳

## Tools being evaluated
- GitHub `Copilot` (Live Demo)
- JetBrains `AI Assistant` (similar functionalities)

## Common features
- 19 USD / month / user
- based on OpenAI (support the same list of languages)
- integrated with IDE (VS Code, JetBrains products)

[comment]: <> (https://controlant.atlassian.net/servicedesk/customer/portal/30/PRS-2256)  
[comment]: <> (https://controlant.atlassian.net/servicedesk/customer/portal/30/PRS-2388)
""",
    },
    "2. Demo": {
        "align": "justify",
        "text": """
# Demo of GitHub Copilot

## VS Code Plugins:

- GitHub `Copilot` - autocomplete-style suggestions
- GitHub `Copilot Chat` - conversational AI assistance

## Sample project

- Simple `Todo` list application
- `Python Flask` web application
- `SQLAlchemy` ORM plus `SQLite` database
- `semantic-ui` CSS framework

[comment]: <> (https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
[comment]: <> (https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

""",
    },
    "2. Sample project - rich": {
        "align": "center",
        "text": figlet_gradient("DEMO", gradient="Relay", font="epic"),
        # slant, epic, alligator, block, cosmic, roman, script, rounded
    },
    "2. Shortcuts & UI, Agents": {
        "align": "justify",
        "text": """
## Shortcuts & UI

- `⌃` + `space`     - show suggestions
- `tab`           - accept suggestion
- `esc`           - dismiss suggestion
- `⌃` + `⌘` + `I`     - Opens the Chat view
- `⇧` + `⌘` + `I`     - Opens the Quick Chat
- `⌃` + `L`         - Clears the Chat view
- `⌘` + `↓`         - Moves keyboard focus to the Chat view input box
- `RMB` > `Copilot` - context menu 

## Agents

- `@workspace` - suggest code from your workspace
- `@vscode`    - knows about features in the VS Code editor itself
- `@terminal`  - has context about the integrated terminal shell and its contents (`#terminalLastCommand`)

""",
    },
    "2. Inline": {
        "align": "justify",
        "text": """
## Inline hints

- sort by _title_ (list)
- sort by _title_ (query)
- check if id is _None_ (update)

        
""",
    },
    "2. Slash commands": {
        "align": "justify",
        "text": """
## Slash commands

- `/explain` - explain the code

```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

- `/fix` - fix the code

```python
todo is not deleted in db
```

""",
    },
    "2. Slash commands 2": {
        "align": "justify",
        "text": """
## Slash commands - continued
- `/doc` - auto generate docstring

```python
class Todo(db.Model):
```

- `/tests` - auto generate unit tests

```bash
python -m unittest ./test_app.py
# or
pytest -r  test_app.py
```
""",
    },
    "2. Slash commands 3": {
        "align": "justify",
        "text": """
## Slash commands - continued

- `/chat` - chat with Copilot

```python
# example 1: separate _id_ and _title_
```

```python
# example 2: make _id_ bigger and blue
```

```python
# example 3: add new route that returns all todos as json
```

```python
# example 4: rewrite selected function by adding type hints to all variables

@app.get("/update/<int:todo_id>")
def update(todo_id):
```
        
""",
    },
    "3. Bonus - rich": {
        "align": "center",
        "text": figlet_gradient("BONUS", gradient="Orange Coral", font="slant"),
        # slant, epic, alligator, block, cosmic, roman, script, rounded
    },
    
    "3. Bonus": {
        "align": "justify",
        "text": """
## __BONUS__ Demo of local code assistant

Toolchain:

- `Continue` - VS Code plugin
- `Ollama`   - framework for running local LLM models
- `codelama` - open source, free LLM model by Meta

[comment]: <> (https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
[comment]: <> (https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)

""",
    },
    "The End - rich": {
        "align": "center",
        "text": figlet_gradient("Thank you!", gradient="Bloody Mary", font="roman"),
            #f"[yellow]{pyfiglet.figlet_format('Thank you !', font='twin_cob')}[/]",
        # slant, epic, alligator, block, cosmic, roman, script, rounded
    },
    "PS": {
        "align": "left",
        "text": """
# Post Scriptum

This presentations has been created using [Spiel](www.github.com/JoshKarpel/spiel) - a terminal-based presentation tool for programmers.

You can find the source code of this presentation [here](https://github.com/HubertReX/AI_asissted_coding_presentation).

Why in `Spiel`?
- to **learn** something new
- because I **love** terminal apps ❤️
- it's based on pure code (Python)
- not to be `tool driven` (apps like `PowerPoint` influence the way we create presentations)
""",
    },
#     "First": {
#         "align": "justify",
#         "text": """### Head

# - one
# - two

# ```python
# def fun():
#   pass
  
# if __name__ == "__main__":
#   fun()
# ```""",
#     },
#     "Second": {
#         "align": "justify",
#         "text": """## Head

# this is long text __bold__ and _italic_

# **bold** ==highlight==   ~~strike~~        
#         """,
#     },
#     "Third": {
#         "align": "justify",
#         "text": """# title
# :::info
# This is a warning!

# :::

# [link](https://www.google.com)
#         """,
#     },
}
# @deck.slide(title="Slide 1 Welcome")
# def slide_1() -> RenderableType:
#     return "Hello World!"

def pad_markdown(markup: str, justify="center") -> RenderableType:
    return Padding(Markdown(dedent(markup), justify=justify, ), pad=(0, 5))

def make_slide_txt(
    title_prefix: str,
    text: Text,
    align="center", 
    v_align="middle"
) -> Slide:
    def content() -> RenderableType:
        return Align(Text.from_markup(text), align=align, vertical=v_align)

    return Slide(title=f"{title_prefix}", content=content, bindings=CUSTOM_BINDINGS)

def make_slide_img(
    title_prefix: str,
    image_path: Path,
    align="center", 
    v_align="middle"
) -> Slide:
    def content() -> RenderableType:
        img = Image.from_file(image_path)
        
        return Align.center(img, vertical="middle") 
    
        return Panel.fit(
                Align.center(img, vertical="middle"),
                subtitle=image_path.name,
                box=HEAVY,
                padding=0,
            )

    return Slide(title=f"{title_prefix}", content=content, bindings=CUSTOM_BINDINGS)

def make_slide_md(
    title_prefix: str,
    text: RenderableType,
    align="center", 
    v_align="middle"
) -> Slide:
    def content() -> RenderableType:
        return Align(pad_markdown(text, justify=align), vertical=v_align)

    return Slide(title=f"{title_prefix}", content=content, bindings=CUSTOM_BINDINGS) # 


# deck.add_slides(
    # Slide(title="Welcome", content=Image.from_file(CYBORG_DEV_IMAGE_PATH)),
    # make_slide_img(title_prefix="Image", image_path=CYBORG_DEV_IMAGE_PATH),
    # make_slide_txt(title_prefix="First", text=Text.from_markup("[blue on white]Foo[/]\n\n(*) one\n(*) two\n(*) three")),
    # make_slide_md(title_prefix="Second", text="### Head\n\n- one\n- two\n\n```python\ndef fun():\n  pass\n```", align="justify", ),
    # make_slide_txt(title_prefix="Third", text=Text("Baz", style=Style(color="green", bgcolor="white")), v_align="top"),
# )

for title, content in CONTENT.items():
    if "IMAGE" in title.upper():
        deck.add_slides(make_slide_img(title_prefix=title, **content))
    elif "RICH" in title.upper():
        deck.add_slides(make_slide_txt(title_prefix=title, **content))
    else:
        deck.add_slides(make_slide_md(title_prefix=title, **content))

if __name__ == "__main__":
    present(__file__)
    # from rich import print
    # for key in good_gradients.keys():
    #     print(f"{key}:\n {figlet_gradient('DEMO', gradient=key, font='roman')}")
    
    # print(app.deck._slides[0].bindings)
    # app.action_last_slide()
    # app.run()
