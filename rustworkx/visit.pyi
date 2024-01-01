# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# This file contains only type annotations for PyO3 functions and classes
# For implementation details, see visit.py

from typing import Generic, TypeVar

class StopSearch(Exception): ...
class PruneSearch(Exception): ...

_T = TypeVar("_T")

class BFSVisitor(Generic[_T]):
    def discover_vertex(self, v: int): ...
    def finish_vertex(self, v: int): ...
    def tree_edge(self, e: tuple[int, int, _T]): ...
    def non_tree_edge(self, e: tuple[int, int, _T]): ...
    def gray_target_edge(self, e: tuple[int, int, _T]): ...
    def black_target_edge(self, e: tuple[int, int, _T]): ...

class DFSVisitor(Generic[_T]):
    def discover_vertex(self, v: int, t: int): ...
    def finish_vertex(self, v: int, t: int): ...
    def tree_edge(self, e: tuple[int, int, _T]): ...
    def back_edge(self, e: tuple[int, int, _T]): ...
    def forward_or_cross_edge(self, e: tuple[int, int, _T]): ...

class DijkstraVisitor(Generic[_T]):
    def discover_vertex(self, v: int, score: float): ...
    def finish_vertex(self, v: int): ...
    def examine_edge(self, e: tuple[int, int, _T]): ...
    def edge_relaxed(self, e: tuple[int, int, _T]): ...
    def edge_not_relaxed(self, e: tuple[int, int, _T]): ...