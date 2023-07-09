import asyncio
import logging
from grpc import aio

from grpc_hub import service_pb2_grpc as grpc_service
from grpc_hub import service_pb2 as grpc_messages

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


async def run():
    async with aio.insecure_channel('localhost:50051') as channel:
        stub = grpc_service.SimpleServiceStub(channel)
        while True:
            request = grpc_messages.PingMessage(body="Ping")
            logger.info("Sent request: %s", request.body)
            response = await stub.Ping(request)
            logger.info("Got response: %s", response.body)
            await asyncio.sleep(1)


if __name__ == '__main__':
    logger.info("Start GRPC client.")
    asyncio.run(run())
