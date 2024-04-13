from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Mega Chat',
        docs_url='/api/docs',
        description="A simple chat application using FastAPI, Websockets and Kafka",
        debug=True,
    )

