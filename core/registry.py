from collections import defaultdict
import weakref
import fnmatch


class SimRegistry:
    """
        ## Simulation Registry for Objects and Signals
    """

    def __init__(self):
        self._objects = {}
        self._names = weakref.WeakKeyDictionary()
        self._counters = defaultdict(int)


    def _register_obj(self, obj : object, name : str = None):

        prefix = obj.__class__.__name__
        idx = self._counters[prefix]
        self._counters[prefix] += 1

        if name is None:
            name = f"{prefix}{idx}"

        if name in self._objects:
            raise ValueError(
                f"Object '{name}' already registered"
            )

        # Forward LookUp
        self._objects[name] = obj

        # Reverse LookUp
        self._names[obj] = name

        return name



    def register(self, obj : object, name : str = None):

        name = self._register_obj(obj, name)
        # print("Registry Add: ", name)

        if hasattr(obj, "ports"):
            for ptype, ports in obj.ports().items():
                for pname, port in ports.items():
                    self.register(
                        port,
                        f"{name}.{ptype}.{pname}"
                    )


        return name


    def get(self, name : str):
        return self._objects[name]


    def find(self, name : str):
        return self._objects.get(name)


    def all(self):
        return self._objects.values()


    def match(self, pattern : str):
        return {
            n: o for n, o in self._objects.items()
            if fnmatch.fnmatch(n, pattern)
        }


    def name_of(self, obj : object):
        return self._names[obj]