from flask import Flask, request, jsonify

app = Flask(book_ticket_)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    
    # Process the booking data here (e.g., save to a database, send an email, etc.)
    print(f"Received booking: {data}")
    
    return jsonify({'message': 'Ticket booked successfully!'})

if _name_ == '_main_':
    app.run(debug=True)