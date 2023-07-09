import asyncio
import logging

from grpc import aio

from grpc_hub import service_pb2_grpc as grpc_service
from grpc_hub import service_pb2 as grpc_messages

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)

_cleanup_coroutines = []


class SimpleServiceServicer(grpc_service.SimpleServiceServicer):
    async def Ping(self, request, context):
        logger.info("Get request: %s", request.body)
        return grpc_messages.PingMessage(body="Pong.")


async def serve() -> None:
    server = aio.server()
    grpc_service.add_SimpleServiceServicer_to_server(SimpleServiceServicer(), server)
    server.add_insecure_port('127.0.0.1:50051')
    await server.start()

    await server.wait_for_termination()


if __name__ == '__main__':
    logger.info("Start GRPC server.")
    asyncio.run(serve())
