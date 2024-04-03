# run without an account
textual-web --config ganglion.toml

# debug
#DEBUG=1 textual-web --config ganglion.toml

# create account
# textual-web --signup

# run with account
# add this to ganglion.toml
# [account]
# api_key = "<YOUR_API_KEY"

#  or

# export TEXTUAL_WEB_API_KEY="<YOUR_API_KEY"
# envsubst < ganglion.toml.tmpl > ganglion_parsed.toml
# textual-web --config ganglion_parsed.toml
# rm ganglion_parsed.toml
