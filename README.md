# Rich and Texutal presentation

## how to run presentation

```bash
# get pipx from https://pipx.pypa.io/stable/
# install frogmouth
pipx install frogmouth

# start presentation
frogmouth PRESENTATION.md
```

## how to run examples

```bash
# create venv
python -m venv .venv
# activate venv
source .venv/bin/activate # on Linux/MacOS
# or
.venv\Scripts\activate # on Windows
# install packages
pip install -r requirements.txt

# for optional web demo
pipx install textual-web


# demos
./rich_demo.sh
./textual_demo.sh

# export PATH=$PATH:./samples_trogon
cd samples_trogon
python todo_list_manager.py tui
cd ..

# optional
./serve_textual_web.sh

# check other scripts in sample_* folders

```
