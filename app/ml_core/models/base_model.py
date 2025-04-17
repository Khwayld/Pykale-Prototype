from abc import ABC, abstractmethod


class BaseModel(ABC):
    name = "base"

    @classmethod
    @abstractmethod
    def supported_datasets(cls):
        """
        A list of supported datasets.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def build(cls, **kwargs):
        """
        Returns a trainer.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def load(cls, ckpt, **kwargs):
        """
        Loads the trainer from a lightning checkpoint.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_dataloader(cls):
        """
        Returns a torch dataloader.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def render_ui(cls, ckpt):
        """
        Renders the UI component for the trainer.
        """
        raise NotImplementedError

