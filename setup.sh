mkdir -p ~/.streamlit/
echo "
[general]
email = "anirudhv2001@ymail.com"
" > ~/.streamlit/credentials.toml
echo "
[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml
