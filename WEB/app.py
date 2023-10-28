from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resultados')
def resultados():
    return render_template('resultados.html')

@app.route('/pesquisa', methods=['POST'])
def pesquisa():
    termo_pesquisa = request.form.get('termo_pesquisa')
    return redirect(url_for('mostrar_resultados', termo_pesquisa=termo_pesquisa))

@app.route('/resultados/<termo_pesquisa>')
def mostrar_resultados(termo_pesquisa):
    return render_template('resultados.html', termo_pesquisa=termo_pesquisa)

if __name__ == '__main__':
    app.run(debug=True)