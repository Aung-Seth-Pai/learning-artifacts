## This is a real world example use-case of decorator pattern

from abc import ABC, abstractmethod

# --- 1. The Common Interface ---
class DataStream(ABC):
    """The common interface for our export pipeline."""
    @abstractmethod
    def write(self, data: str) -> str:
        pass

# --- 2. The Concrete Component ---
class SimpleReportGenerator(DataStream):
    """The core object that simply outputs the raw string."""
    def write(self, data: str) -> str:
        return f"RAW_DATA: {data}"

# --- 3. The Base Decorator ---
class StreamDecorator(DataStream):
    def __init__(self, stream: DataStream):
        self._stream = stream
    def write(self, data: str) -> str:
        return self._stream.write(data)

# --- 4. Concrete Decorator A: HTML Formatter ---
class HTMLDecorator(StreamDecorator):
    def write(self, data: str) -> str:
        base_data = super().write(data)
        html_data = f"<p> {base_data} </p>"
        return html_data

# --- 5. Concrete Decorator B: Encryptor (Simulated) ---
class EncryptDecorator(StreamDecorator):
    def write(self, data: str) -> str:
        base_data = self._stream.write(data)
        encrypted_data = base_data[::-1]
        return encrypted_data


# ---- define Client code -----
def main():
    my_data_string = "Hello World"

    # construct decorators
    base_stream = SimpleReportGenerator()
    html_stream = HTMLDecorator(base_stream)
    encrypted_html_stream = EncryptDecorator(html_stream)
    
    print(encrypted_html_stream.write(my_data_string))
if __name__ == "__main__":
    main()