#Python 3.4.4

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket()
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
reference_map = {
    """/about/aboutme.html""": """C:\\Users\\khoramus\\Desktop\\web\\Exercise1-1\\myproject\\about\\aboutme.html""",
    '''/index.html''': '''C:\\Users\\khoramus\\Desktop\\web\\Exercise1-1\\myproject\\index.html''',
    '''/''': '''C:\\Users\\khoramus\\Desktop\\web\\Exercise1-1\\myproject\\index.html'''
}
while True:
    conn, address = s.accept()
    directory = conn.recv(BUFFER_SIZE).decode('utf-8').split(None, 2)[1]
    path = reference_map.get(directory, '');
    if path:
        HTML_file = open(path, 'rb')
        file_data = HTML_file.read()
        conn.send(file_data)
        HTML_file.close()
    else:
        conn.send(b'404')
conn.close()
