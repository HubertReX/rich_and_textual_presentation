# import asyncio

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
    "2. Sample project": {
        "align": "center",
        "text": """
DEMO
""",
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
    "The End": {
        "align": "center",
        "text": """
__Thank You!__
""",
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
        return Align(text, align=align, vertical=v_align)

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
    else:
        deck.add_slides(make_slide_md(title_prefix=title, **content))

if __name__ == "__main__":
    present(__file__)
    
    # print(app.deck._slides[0].bindings)
    # app.action_last_slide()
    # app.run()
