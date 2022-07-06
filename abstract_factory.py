from dataclasses import dataclass


@dataclass
class SocketH:
    """One of the objects to be returned"""

    def action(self) -> str:
        return f"Connection: http"


class SocketHFactory:
    """Concrete factory for http connection"""

    def get_connection(self) -> SocketH:
        """Return a connection object"""
        return SocketH()

    def get_request(self) -> str:
        """Returns a get request object"""
        return f"GET request"


@dataclass
class SocketF:
    """One of the objects to be returned"""

    def action(self) -> str:
        return f"Connection: ftp"


class SocketFFactory:
    """Concrete factory for ftp connections"""

    def get_connection(self) -> SocketH:
        """Return a connection object"""
        return SocketF()

    def udp_request(self) -> str:
        """Returns a UDP protocol object"""
        return f"UDP protocol"


@dataclass
class Connections:
    _connection_factory: SocketHFactory | SocketFFactory = None

    def show_connection(self) -> None:
        """Utility method to display the details of the object returned from the connection factory"""
        connection = self._connection_factory.get_connection()
        request = (
            self._connection_factory.get_request()
            if isinstance(self._connection_factory, SocketHFactory)
            else self._connection_factory.udp_request()
        )

        print(f"Connection: {connection}")
        print(f"Action: {connection.action()}")
        print(f"Request: {request}")


# create a concrete factory
factory_a = SocketHFactory()
factory_b = SocketFFactory()

conn = Connections(factory_a)
conn.show_connection()

conn = Connections(factory_b)
conn.show_connection()
