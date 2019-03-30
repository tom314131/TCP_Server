# TCP_Server
The client send the server a name of a file that he wants to download in a specific input format.
If the file exist the server send a message of "200 OK" and send the file to the client.
If the file doesn't exist we send a message of "404 Not Found"
The server can send other messages to the client due to his request for example:
" 301 Moved Permanently (and location)"
