"""Base class for memory providers."""
import abc
from config import AbstractSingleton, Config
import openai
import time
from openai.error import APIError
cfg = Config()



def get_ada_embedding(text: str) -> list:
    retries = 3
    for i in range(retries):
        try:
            return openai.Embedding.create(input=[text], model="text-embedding-ada-002")["data"][0]["embedding"]
        except APIError as e:
            if i < retries - 1:
                print(f"Error occurred while fetching embedding. Retrying {i + 1}/{retries}...")
                time.sleep(2 ** i)  # Exponential backoff
            else:
                raise e


class MemoryProviderSingleton(AbstractSingleton):
    @abc.abstractmethod
    def add(self, data):
        pass

    @abc.abstractmethod
    def get(self, data):
        pass

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def get_relevant(self, data, num_relevant=5):
        pass

    @abc.abstractmethod
    def get_stats(self):
        pass
