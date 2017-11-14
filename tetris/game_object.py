from .game_interface import GameInterface


class Vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key in (0, "x"):
            return self.x
        if key in (1, "y"):
            return self.y
        raise KeyError("Vector2 has no key %s" % key)

    def __setitem__(self, key, value):
        raise RuntimeError("No __setitem__ allowed on Vector2")

    def __len__(self):
        return 2


class GameObject(object):

    def __init__(self, game_interface, *args, **kwargs):
        assert isinstance(game_interface, GameInterface)
        self.game_interface = game_interface

    def load_content(self, content_loader):
        pass

    def update(self):
        pass

    def get_render_layer(self):
        pass

    def render(self, screen):
        pass

    def destroy(self):
        self.game_interface.destroy(self)