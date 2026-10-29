from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Menu-Driven Calculator — V1</h2>
<form method="post">
  <input name="a" type="number" step="any"
         placeholder="First number" required>
  <input name="b" type="number" step="any"
         placeholder="Second number" required>
  <select name="op">
    <option value="add">Addition</option>
    <option value="sub">Subtraction</option>
  </select>
  <button type="submit">Calculate</button>
</form>
<p>{{ result }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)