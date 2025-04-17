class ModelRegistry:
    """"""

    models = {}

    @classmethod
    def register(cls, model_cls):
        cls.models[model_cls.name] = model_cls
        return model_cls          

    @classmethod
    def list_models(cls):
        return sorted(cls.models)

    @classmethod
    def get(cls, name):
        return cls.models[name]
