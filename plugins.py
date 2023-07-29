from abc import ABCMeta, abstractmethod
import inspect


class RegistryMeta(ABCMeta):
    """Это метакласс"""
    
    _registry_formats = {}

    def __new__(mcs, name, bases, attrs):
        cls: 'BasePlugin' = super().__new__(mcs, name, bases, attrs)

        if inspect.isabstract(cls):
            return cls

        for media_format in cls.supported_formats:
            if media_format in mcs._registry_formats:
                raise ValueError(f"Format {media_format} already registered")
            mcs._registry_formats[media_format] = cls
        return cls

    @classmethod
    def get_plugin(mcs, media_format: str):
        try:
            return mcs._registry_formats[media_format]
        except KeyError:
            raise RuntimeError(f"Plugin for {media_format} is not defined!")

    @classmethod
    def show_registry(mcs):

        from pprint import pprint

        pprint(mcs._registry_formats)


class BasePlugin(metaclass=RegistryMeta):
    @property
    @abstractmethod
    def supported_formats(self) -> list:
        pass

    @abstractmethod
    def run(self, input_data: dict) -> None:
        pass


class VideoPlugin(BasePlugin):
    supported_formats = ['mov', 'mkv']
    
    def run(self):
        print("video plugin")

class ImagePlugin(BasePlugin):
    supported_formats = ['jpg', 'gif']
    
    def run(self):
        ...


plugin = VideoPlugin()
plugin.supported_formats
RegistryMeta.show_registry()
plugin_class = RegistryMeta.get_plugin('jpg')
print(plugin_class)
# plugin_class = RegistryMeta.get_plugin('avi')

