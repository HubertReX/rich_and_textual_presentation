clear

# https://unix.stackexchange.com/questions/615060/how-to-trap-exit-unconditionally-even-if-interrupted-in-zsh
# test_trap() {
#     # set -o localoptions -o localtraps
#     set -o localtraps
#     # trap 'echo "I am exiting."' EXIT
#     trap '' INT

#     echo start
#     python -m rich.progress
#     echo end
# }


# echo "returned with: $?"
# read -s -n 1 -p "Press any key to continue . . ."
# exit

function run_step(){
    rich -u
    echo $*
    read -s -n 1 -p "Press any key to continue . . ."
    echo ""
    # echo $1 $2 $3 $4 $5 '"'$6'"' $7 '"'$8'"'
    # trap - SIGINT
    # $1 $2 $3 $4 $5 '"'$6'"' '$7' '"'$8'"'
    $*
    # trap '' SIGINT
}

run_step python -m rich

run_step python -m rich.markup

run_step python samples_rich/table_movie.py

# run_step python samples_rich/fullscreen.py

run_step python samples_rich/tree.py .

run_step cat sample_syntax.py

run_step python -m rich.syntax sample_syntax.py  

run_step cat sample_markdown.md
run_step python -m rich.markdown sample_markdown.md

run_step cat sample_json.json
run_step python -m rich.json sample_json.json
# # -----
# run_step python -m rich.live

# # run_step python -m rich.progress
# # run_step python -m rich.spinner
# # -----
run_step python -m rich.traceback

run_step python -m rich.syntax -x python ~/.pythonrc && python

run_step less sample_csv.csv
echo ""
run_step rich --pager sample_csv.csv

run_step rich --help
rich -u
echo 'rich -a rounded -c -S "yellow on blue" -p "[yellow]Hello[/]"'
read -s -n 1 -p "Press any key to continue . . ." && echo "" && rich -u
rich -a rounded -c -S "yellow on blue" -p "[yellow]Hello[/]"


