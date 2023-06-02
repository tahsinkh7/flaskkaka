from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Toffee"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
from flask import Flask, make_response import requests import os app = Flask(name) API_ENDPOINT = "https://bldcmprod-cdn.toffeelive.com/" headers = { "Cookie": "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1687300795:KeyName=prod_linear:Signature=nIzw2EzgOAck_WNIgmnHYOrTD8taW6g5MjRupBozwsUuoNhnncaFn9SnEbrrwZOjfwqAHXIAyWElcYqgKnt1Ag" } @app.route("/") def credit(): return "(Toffee-API) Made With ❤️ By Proximity BD " @app.route("/auto/<string:channel_id>.m3u8") def handle_auto(channel_id): response = requests.get(API_ENDPOINT + f"cdn/live/{channel_id}/playlist.m3u8", headers=headers) myresponse = make_response(response.text.replace("../slang/", "/single/slang/").replace("?", "-")) myresponse.headers["Content-Type"] = "application/vnd.apple.mpegurl" return myresponse @app.route("/single/<path:path>") def handle_single(path): single_url = API_ENDPOINT + "cdn/live/" + path.replace("-", "?") print(single_url) response = requests.get(single_url, headers=headers) myresponse = make_response(response.text.replace("/live/", f"{API_ENDPOINT}/live/")) myresponse.headers["Content-Type"] = "application/vnd.apple.mpegurl" return myresponse if name == "main": app.run(debug=True, port=os.getenv("PORT", default=5000))
