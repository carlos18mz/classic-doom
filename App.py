import http.server
PORT = 3001

HandlerClass = http.server.SimpleHTTPRequestHandler
HandlerClass.extensions_map[".js"] = "text/javascript"

print(f"http://localhost:{PORT}")
http.server.test(HandlerClass, port=PORT)
