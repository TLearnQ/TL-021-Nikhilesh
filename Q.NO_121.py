books = []

def handle_request(request):
    parts = request.split()

    if len(parts) < 2:
        return "Invalid request format"

    method = parts[0]
    path = parts[1]

    if method == "GET" and path == "/items":
        return books

    elif method == "POST" and path == "/items":
        if len(parts) < 3:
            return "Missing book name"
        book_name = parts[2]
        books.append(book_name)
        return f"Book '{book_name}' added"

    elif method == "GET" and path == "/count":
        return len(books)
    else:
        return "Invalid method or path"

print(handle_request("GET /items"))
print(handle_request("POST /items test1"))
print(handle_request("GET /items"))
print(handle_request("POST /items"))
print(handle_request("POST /items test2"))
print(handle_request("GET /items"))
print(handle_request("GET /count"))
print(handle_request("PUT /items"))   