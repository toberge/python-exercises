#!/usr/bin/env python3
import argparse
import socket
import threading
import re

content_root = '.'
# Valid formats in accept header in request
ACCEPTED_FORMATS = {'text/html', 'text/plain', 'image/jpeg'}

# Map of provided file types to their HTTP content-typpe
FILE_TYPES = {
    'html': 'text/html',
    'htm': 'text/html',
    'txt': 'text/plain',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    '/': 'text/html'
}

def read_file_if_exists(filename):
    """Attempt to read file, return None if not existing or of invalid type"""
    # / means index file
    if filename == '/':
        filename = '/index.html'

    # check file type
    if not filename.split('.')[-1].lower() in FILE_TYPES:
        return None

    try:
        # Read binary file -> lets us return images too!
        with open(content_root + filename, 'rb') as file:
            return file.read()
    except OSError as error:
        # return a falsy value on error
        print(error)
        return None

def identify_content_type(data):
    """Formatted like text/html,application/xhtml+xml etc.
    Split on comma and check if acceptable
    """
    # Read formats
    for form in data.split(','):
        if form in ACCEPTED_FORMATS:
            return True
    else: # no matching format!
        return False

HEADER_HANDLERS={
    'Accept': identify_content_type
}

def headers_are_valid(headers: list):
    """Check if headers are valid according to a set of tests"""
    for header in headers:
        # Go through headers as key-value pairs
        [name, data] = header.split(': ')
        try:
            # Perform test
            if not HEADER_HANDLERS[name](data):
                return False
        except KeyError:
            # no handler for that kind of header, go on
            continue
    return True

def is_valid_request_line(line):
    """Checks if the first line of the request indicates a proper GET request"""
    return re.match(r'^GET \/([^\/]+.[^\/]+)? HTTP/\d.\d$', line)

def assemble_headers(path, length):
    """Supporting only two header fields, as requested
    Content-type with proper HTTP content-type string
    Content-length with the number of bytes in the requested file
    """
    filetype = path.split('.')[-1].lower()
    return [f'Content-type: {FILE_TYPES[filetype]}', f'Content-length: {length}']

def inspect_request(lines) -> (str, bytes):
    """Inspect request and return a properly formatted response + any content"""
    # Validate first line and headers
    if is_valid_request_line(lines[0]) and headers_are_valid(lines[1:-2]):

        path = lines[0].split()[1]
        # check that the path is valid: A path is valid if it is in the root folder but *no deeper*
        if path.count('/') > 1:
            # do not return stuff in subfolders!
            print(f'Warning: Client tried to access file in subfolder: {path}')
            return 'HTTP/1.1 403 Forbidden\r\n\r\n', None
        
        # Open content
        content = read_file_if_exists(path)
        if not content: # not found or invalid type
            print(f'Did not find client\'s requested file: {path}')
            return 'HTTP/1.1 404 Not found\r\n\r\n', None

        # Use CRLF newlines
        headers = '\r\n'.join(assemble_headers(path, len(content)))
        return f'HTTP/1.1 200 Ok\r\n{headers}\r\n\r\n', content
    else:
        print(f'Recieved invalid request: {lines[0]}')
        return 'HTTP/1.1 400 Invalid request\r\n\r\n', None

def handle(connection: socket.socket, remote):
    """Handle a connection by responding to its *single* request"""
    with connection:
        connection.settimeout(10)
        # Receive request
        data = connection.recv(4096)
        if len(data):
            # if we recieved any data
            lines = str(data, encoding='UTF-8').split('\r\n')
            response, content = inspect_request(lines)
            if content:
                connection.sendall(bytes(response, 'UTF-8') + content)
            else:
                connection.sendall(bytes(response, 'UTF-8'))
        else:
            connection.sendall(bytes('HTTP/1.1 400 Invalid request\r\n\r\n', 'UTF-8'))

def serve(port):
    """Create socket server on default IP and provided port"""
    with socket.create_server(('', port)) as server:
        server.listen(1)
        while True:
            connection, remote = server.accept()
            # Handle incoming connections in their own threads
            thread = threading.Thread(None, handle, args=(connection, remote))
            thread.start()

if __name__ == "__main__":
    # Parse args using ArgumentParser
    # (not by parsing sys.argv directly since this case is more complex)
    parser = argparse.ArgumentParser(description='A simple HTTP server.')
    # Required port argument
    parser.add_argument('-p', dest='port', type=int, required=True,
                        help='What port the server should listen on')
    # Required content root argument
    parser.add_argument('-r', dest='root', required=True,
                        help='Root directory of web content')

    # parse_args() calls exit() if args are invalid
    args = parser.parse_args()
    print('Shall listen on', args.port, 'and serve', args.root)
    content_root = args.root
    serve(args.port)