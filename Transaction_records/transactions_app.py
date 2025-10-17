from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# To implement a Read operation (back to home page, list of all transactions)

@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)  


# Create operation (Route to allow users to enter new transactions)

# This will involve handling both GET and POST HTTP requests 
# GET for displaying the form to the user 
# POST for processing the form data sent by the user.

@app.route('/add', methods = ['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template('form.html')           # Form to allow input of new transaction
    
    if request.method == 'POST':
        transaction = {
            'id' : (len(transactions)) + 1,           # Create new ID based on length of transactions list
            'date' : request.form['date'],            # User enters date
            'amount' : float(request.form['amount'])  # User enters amount, converts to float
        }

        transactions.append(transaction)              # Append back to transactions list
        return redirect(url_for('get_transactions'))  # Redirect back to transactions homepage
    

# For the Update operation, route that allows users to update existing transactions.

@app.route('/edit/<int:transaction_id>', methods = ['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction = transaction)       # If the request method is GET, find the transaction with the matching ID and render the edit form, and pass the transaction to be edited
            
    
    if request.method == 'POST':
        date = request.form['date']                        # Get the 'date' field value from the form
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date                 # Update the date field
                transaction['amount'] = amount

                break                                      # Exit the loop once the transaction is found and updated
        
        return redirect(url_for('get_transactions'))
    
    return {'message' : 'Transaction not found'}, 404      # else statement if specified ID is not found


# Delete operation

@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            
            break
    
    return redirect(url_for('get_transactions'))


# Search function

@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    if request.method == 'GET':
        return render_template('search.html')

    if request.method == 'POST':
        min_amount = float(request.form['min_amount'])       # Retrieve min and max amount values from form data
        max_amount = float(request.form['max_amount'])

        filtered_transactions = [                            # Create a new list, filtered_transactions, that contains only the transactions whose amount falls within the specified range. 
            transaction for transaction in transactions
            if max_amount >= transaction['amount'] >= min_amount
        ]

        return render_template('transactions.html', transactions=filtered_transactions)      # Pass the filtered_transactions list to the transactions.html
    

if __name__ == '__main__':
    app.run(debug=True)
                                          