from flask import Flask, redirect, render_template, request, url_for, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-para-desarrollo'

SCORES = {
    "Chispa Unicornio": 0,
    "Senor Meme": 0,
    "Dona Fiesta": 0,
    "Capitan Karaoke": 0,
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form.get("vote")
        
        if vote and vote in SCORES:
            SCORES[vote] += 1
            flash(f"¡Voto registrado para {vote}!", "success")
        return redirect(url_for("index"))

    total_votes = sum(SCORES.values())
    ranking = sorted(SCORES.items(), key=lambda item: item[1], reverse=True)
    
    return render_template("index.html", ranking=ranking, total_votes=total_votes)

@app.route("/reset", methods=["POST"])
def reset_scores():
    for name in SCORES:
        SCORES[name] = 0
    flash("¡Puntuaciones reiniciadas!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)