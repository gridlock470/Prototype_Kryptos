from flask import Flask, render_template
import Ceaser_Cypher

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/encryt', methods = ['POST'])
def encrypt():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400
    
    plain_text = data['text']
    encrypted_text, shift1, shift2 = Ceaser_Cypher(plain_text)
    return jsonify({
        'encrypted': encrypted_text,
        'shift1': shift1,
        'shift2': shift2
    })

if __name__ == '__main__':
    app.run(debug = True)