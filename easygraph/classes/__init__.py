from .directed_graph import DiGraph
from .directed_graph import DiGraphC
from .directed_multigraph import MultiDiGraph
from .graph import Graph
from .graph import GraphC
from .graphviews import *

# from .base import BaseHypergraph
# from .base import load_structure
# from .hypergraph import Hypergraph
from .hypergraph import Hypergraph
from .multigraph import MultiGraph
from .operation import *


try:
    from .base import BaseHypergraph
    from .base import load_structure

except:
    print(
        "Warning raise in module:classes. Please install Pytorch before you use"
        " functions related to Hypergraph"
    )
