from flask import Flask, render_template, request, send_file

from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw", back_color=request.args.get("back",""),fill_color=request.args.get("fill","")), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)