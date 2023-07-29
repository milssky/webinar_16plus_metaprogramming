from typing import Type, TypeVar


class Geometry:
    pass


class Point2D(Geometry):
    pass


T = TypeVar("T", bound=Geometry)
N = TypeVar("N", bound=int | float)
M = TypeVar("M")


def factory_geometry(cls_geometry: Type[T]) -> T:
    return cls_geometry()


geometry: Geometry = factory_geometry(Geometry)
point_2d: Point2D = factory_geometry(Point2D)
