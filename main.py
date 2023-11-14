from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced by database)
books = [
    {"id" : 1, "title" : "Book 1", "author" : "Author 1"},
    {"id" : 2, "title" : "Book 2", "author" : "Author 2"},
    {"id" : 3, "title" : "Book 3", "author" : "Author 3"}
]

# get all books
@app.route("/books", methods = ["GET"])
def get_books():
    return books

# get only one book with id input
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error" : "book doesnt exist"} 

# create a book
@app.route("/books", methods = ["GET"])
def create_book():
    new_book = {"id" : len(books)+1, "title" : request.json["title"], "author" : request.json["author"]}
    books.append(new_book)
    return books

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)