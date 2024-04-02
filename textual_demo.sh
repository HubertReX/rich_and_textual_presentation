clear

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

cd samples_textual

run_step python -m textual
run_step textual easing
run_step python calculator.py
run_step python calculator.py --inline
run_step python code_browser.py
run_step python markdown.py

# run_step python calculator.py --inline
run_step ./in.py pride.py
