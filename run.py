from app import app

with app.app_context():
    app.run(host="0.0.0.0", port=3001, debug=True)
