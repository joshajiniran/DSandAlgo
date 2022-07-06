from collections import defaultdict
from dataclasses import dataclass


def default_conn():
    return SocketH("http_connection")


@dataclass
class SocketH:
    """Class connection example for http"""

    name: str

    def action(self):
        return f"Connection: {self.name}"


@dataclass
class SocketF:
    """Class connection example for ftp"""

    name: str

    def action(self) -> str:
        return f"Connection: {self.name}"


def get_connection(conn: str = "http") -> SocketH | SocketF:
    connections = defaultdict(default_conn)
    connections.update(
        {
            "http": SocketH("http_connection"),
            "ftp": SocketH("ftp_connection"),
        }
    )

    return connections[conn]


if __name__ == "__main__":
    http_s = get_connection("http")
    http_f = get_connection("ftp")

    print(http_s.action())
    print(http_f.action())

    http_n = get_connection("socket_stream")
    print(http_n.action())
    # breakpoint()
