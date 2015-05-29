from .spry import Session


def get(url, path, threads=50, start=False):
    session = Session(url, path, threads)

    if start == True:
        session.start()

    return session