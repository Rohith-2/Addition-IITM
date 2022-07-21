mkdir -p ~/.streamlit/
echo "
[general]n
email = "anirudhv2001@ymail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml
