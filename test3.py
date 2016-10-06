import pytest
from itertools import chain
import json


class Component:
    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list


    def my_method(self, obj):
        result = {'Potential': [],
                  'Algorithm': []}
        for alg in self.algorithm_list:
            spec = alg.SPECIFICATION

            if isinstance(spec, dict) and spec:
                result['Potential'].append(self.__get_class_string__(spec, obj))
                result['Algorithm'].append(self.__get_algorithm__(alg, spec, obj))
        return result

    def __get_class_string__(self, spec, obj):
        result = ['/' + obj.__name__]
        if isinstance(spec, dict):
            lis = spec.get(obj)
            for clazz in lis:
                result.append('/' + obj.__name__ + '/' + clazz.__name__)
            keys = spec.keys()
            for key in keys:
                if key != obj:
                    lis = spec.get(key)
                    for clazz in lis:
                        result.append('/' + obj.__name__ + '/' + key.__name__ + '/' + clazz.__name__)
        return result

    def __get_algorithm__(self, alg, spec, entry):
        if spec:
            dic = {alg.__class__.__name__: {'/' + entry.__name__: []}}
            if isinstance(dic, dict):
                lis = spec.get(entry)
                for clazz in lis:
                    dic[alg.__class__.__name__]['/' + entry.__name__].append(
                        '/' + entry.__name__ + '/' + clazz.__name__)
                keys = spec.keys()
                for key in keys:
                    if key != entry:
                        lis = spec.get(key)
                        dic[alg.__class__.__name__].update({'/' + entry.__name__ + '/' + key.__name__: []})
                        for clazz in lis:
                            dic[alg.__class__.__name__]['/' + entry.__name__ + '/' + key.__name__].append(
                                '/' + entry.__name__ + '/' + key.__name__ + '/' + clazz.__name__)
            return dic
        else:
            return {}


class Apple:
    pass


class Orange:
    number = None

    def __init__(self, number):
        self.number = number


class Lemon:
    pass


class FirstAlgorithm:
    SPECIFICATION = {
        Orange: [Apple],
        Lemon: [Orange, Apple]
    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [Apple() for _ in range(Orange.number)]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}

    def __call__(self, source_object):
        return []


component = Component(FirstAlgorithm(), EmptyAlgorithm())



print(json.dumps(
    component.my_method(Lemon),
    indent=4
))



def test_my_metod():
    component = Component(FirstAlgorithm(), EmptyAlgorithm())
    out = component.my_method(Lemon)
    assert(out == {'Algorithm': [{'FirstAlgorithm': {'/Lemon': ['/Lemon/Orange', '/Lemon/Apple'], '/Lemon/Orange': ['/Lemon/Orange/Apple']}}], 'Potential': [['/Lemon', '/Lemon/Orange', '/Lemon/Apple', '/Lemon/Orange/Apple']]})