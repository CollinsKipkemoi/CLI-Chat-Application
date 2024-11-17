# CLI Chat Application

A simple command-line chat application built with Python using sockets and threading for real-time communication between a server and client.

## Features

- Real-time bidirectional communication
- Support for multiple client connections
- Clean exit mechanism with 'bye' command
- Cross-platform compatibility (Windows/Unix)
- Clear console interface
- Graceful handling of unexpected disconnections

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CLI-Chat-Application.git
cd CLI-Chat-Application
```

## Usage

1. Start the server:
```bash
python server.py
```

2. Start the client in a different terminal:
```bash
python client.py
```

3. Start chatting:
- Type your message and press Enter to send
- Type 'bye' to exit the chat
- The server can shut down all connections by typing 'bye'

## How It Works

### Server (server.py)
- Listens on port 5000
- Handles multiple client connections using select
- Broadcasts messages to connected clients
- Manages client disconnections gracefully

### Client (client.py)
- Connects to the server on localhost:5000
- Uses threading for simultaneous message sending and receiving
- Provides a clean console interface
- Handles server disconnection gracefully

## Commands

- `bye`: Exit the chat (works for both client and server)
- Server's 'bye': Shuts down the server and disconnects all clients
- Client's 'bye': Disconnects the client while keeping the server running

## Error Handling

- Handles unexpected client disconnections
- Manages server shutdown gracefully
- Cleans up resources properly
- Clear error messages for common issues

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details