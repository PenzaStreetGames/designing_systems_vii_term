import asyncio
import socket
import logic

SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 45000


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = (await loop.sock_recv(client, 255)).decode('utf-8')
    print(f'Request from {client.getpeername()} is {request}')
    task_name, *args = request.split()
    response = logic.calculate(task_name, ' '.join(args))
    print(f'Pushing response to {client.getpeername()}: {response}')
    await loop.sock_sendall(client, response.encode('utf-8'))
    print()
    client.close()


async def run_server():
    print('Starting server')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 45000))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        print(f'Receiving request from {client.getpeername()}')
        loop.create_task(handle_client(client))


if __name__ == '__main__':
    asyncio.run(run_server())
