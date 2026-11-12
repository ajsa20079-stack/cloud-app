from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

TITLE = "AisCar"

CARS = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2023, "price_kzt": 17500000, "city": "Астана"},
    {"id": 2, "brand": "Hyundai", "model": "Tucson", "year": 2024, "price_kzt": 16900000, "city": "Алматы"},
    {"id": 3, "brand": "Kia", "model": "K5", "year": 2023, "price_kzt": 14800000, "city": "Астана"},
    {"id": 4, "brand": "Chevrolet", "model": "Onix", "year": 2024, "price_kzt": 7900000, "city": "Шымкент"},
    {"id": 5, "brand": "Chery", "model": "Tiggo 7 Pro", "year": 2024, "price_kzt": 11500000, "city": "Костанай"},
    {"id": 6, "brand": "Lada", "model": "Vesta", "year": 2023, "price_kzt": 6900000, "city": "Караганда"},
]

PAGE = """<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }} — Автосалон</title>
<style>
body{font-family:system-ui,sans-serif;margin:0;background:#f4f6f8;color:#1b2430}
header{background:#0b3d5c;color:#fff;padding:28px 20px;text-align:center}
main{max-width:960px;margin:24px auto;padding:0 16px;display:grid;
grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.card{background:#fff;border-radius:10px;padding:16px;box-shadow:0 1px 4px #0002}
.price{color:#0b7a4b;font-weight:700;font-size:1.15em}
footer{text-align:center;color:#667;padding:20px}
</style></head><body>
<header><h1>{{ title }}</h1><p>Автосалон «Қазақ Авто» — Казахстан</p></header>
<main>
{% for c in cars %}
<div class="card"><h3>{{ c.brand }} {{ c.model }}</h3>
<p>Год: {{ c.year }} · Город: {{ c.city }}</p>
<p class="price">{{ "{:,}".format(c.price_kzt).replace(",", " ") }} ₸</p></div>
{% endfor %}
</main>
<footer>Лабораторная работа №11 · CI/CD</footer>
</body></html>"""


@app.route("/")
def index():
    return render_template_string(PAGE, title=TITLE, cars=CARS)


@app.route("/api/cars")
def cars():
    return jsonify(CARS)


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
