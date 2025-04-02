from flask import Flask, request, render_template, redirect, url_for, session

class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        return f"Your balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrawal successful. {self.display_balance()}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposit successful. {self.display_balance()}"
        else:
            return "Invalid deposit amount."

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            return f"Transfer successful. {self.display_balance()}"
        else:
            return "Invalid transfer amount or insufficient funds."


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy users for testing
users = {
    "user1": User(user_id="user1", pin="1234", balance=1000),
    "user2": User(user_id="user2", pin="5678", balance=500),
    "user3": User(user_id="user3", pin="abcd", balance=2000)
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        pin = request.form['pin']
        user = users.get(user_id)
        if user and user.pin == pin:
            session['user_id'] = user_id
            return redirect(url_for('menu'))
        else:
            return "Invalid user ID or PIN."
    return render_template('login.html')

@app.route('/menu')
def menu():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('menu.html')

@app.route('/balance')
def balance():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = users[session['user_id']]
    return user.display_balance()

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user = users[session['user_id']]
        message = user.withdraw(amount)
        return message
    return render_template('withdraw.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user = users[session['user_id']]
        message = user.deposit(amount)
        return message
    return render_template('deposit.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        recipient_id = request.form['recipient_id']
        amount = float(request.form['amount'])
        user = users[session['user_id']]
        recipient = users.get(recipient_id)
        if not recipient:
            return "Recipient user ID not found."
        message = user.transfer(recipient, amount)
        return message
    return render_template('transfer.html')

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = users[session['user_id']]
    return render_template('history.html', transactions=user.transaction_history)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
