from .spry import Session


def get(url, path, threads=4, start=False):
    session = Session(url, path, threads)

    if start:
        session.start()

    return session
