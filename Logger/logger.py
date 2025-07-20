from abc import ABC, abstractmethod
from enum import Enum

class Level(Enum):
    INFO = 1
    WARNNG = 2
    ERROR = 3
    DEBUG = 4

class Logger(ABC):

    def __init__(self, level: Level):
        self.level = level
        self.next_logger: Logger = None

    @abstractmethod
    def handle_log(self, message, level):

        pass

    def set_next(self, next_logger):
        self.next_logger = next_logger
        return next_logger
    
    def log(self, message, level: Level):
        if self.level.value <= level.value:
            self.handle_log(message, level)
        if self.next_logger:
            self.next_logger.log(message, level)


class ConsoleLogger(Logger):

    def __init__(self, level):
        super().__init__(level)

    def handle_log(self, message, level: Level):
        print(f"Console: {message}, level : {level.value}")


class FileLogger(Logger):

    def __init__(self, level, filename):
        super().__init__(level)
        self.filename = filename

    def handle_log(self, message, level: Level):
        print(f"File: {message}, level : {level.value}")



console = ConsoleLogger(Level.INFO)
file = FileLogger(Level.WARNNG, "abc.txt")

#chain

console.set_next(file)

console.log("Message", Level.WARNNG)

        