## Running application over local: 


## 🌀 clone the entire repo
``` shell
git clone https://github.com/someshfengde/Ask-me-Anything.git
```

## 💱 change directory and install required requirements
``` py
cd ./Ask-me-Anything
pip install -r requirements.txt
```
## 🔐 Adding secret as openai-api key
add following file as `secrets.toml` with your openai api secret.
```
openai_key = "YOUR-OPENAI-API-KEY"
```


## 🏃 Run the frontend 
```
streamlit run frontend.py
```