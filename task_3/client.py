import asyncio
import server


async def send_request(request: str):
    server_socket = f'{server.SERVER_HOSTNAME}:{server.SERVER_PORT}'
    print(f'Connecting to {server_socket}')
    reader, writer = await asyncio.open_connection(
        server.SERVER_HOSTNAME, server.SERVER_PORT
    )
    writer.write(request.encode(encoding='utf-8'))
    await writer.drain()
    response = await reader.readline()
    writer.close()
    print(f'Closing connection {server_socket}')
    return response.decode().strip()


async def main():
    print('Starting client')
    while True:
        task_name_with_args = input('Enter task number with args: ')
        response = await send_request(task_name_with_args)
        print(f'Server response: {response}')
        print()


if __name__ == '__main__':
    asyncio.run(main())
