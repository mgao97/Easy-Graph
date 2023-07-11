import itertools
import time

import easygraph as eg
import networkx as nx

# print(eg.__file__)
from easygraph.functions.basic.predecessor_path_based import predecessor


__all__ = [
    "my_all_shortest_paths",
    "getandJudgeSimpleCircle",
    "getSmallestCycles",
    "StatisticsAndCalculateIndicators",
    "cycle_ratio_centrality",
]


SmallestCycles = set()
NodeGirth = dict()
NumSmallCycles = 0
CycLenDict = dict()
CycleRatio = {}

SmallestCyclesOfNodes = {}  #


def my_all_shortest_paths(G, source, target):
    pred = predecessor(G, source)
    if target not in pred:
        raise nx.NetworkXNoPath(f"Target {target} cannot be reachedfrom given sources")
    sources = {source}
    seen = {target}
    stack = [[target, 0]]
    top = 0
    while top >= 0:
        node, i = stack[top]
        if node in sources:
            yield [p for p, n in reversed(stack[: top + 1])]
        if len(pred[node]) > i:
            stack[top][1] = i + 1
            next = pred[node][i]
            if next in seen:
                continue
            else:
                seen.add(next)
            top += 1
            if top == len(stack):
                stack.append([next, 0])
            else:
                stack[top][:] = [next, 0]
        else:
            seen.discard(node)
            top -= 1


def getandJudgeSimpleCircle(objectList):  #
    numEdge = 0
    for eleArr in list(itertools.combinations(objectList, 2)):
        if G.has_edge(eleArr[0], eleArr[1]):
            numEdge += 1
    if numEdge != len(objectList):
        return False
    else:
        return True


def getSmallestCycles(G):
    NodeNum = G.number_of_nodes()
    DEF_IMPOSSLEN = NodeNum + 1  # Impossible simple cycle length
    Coreness = nx.core_number(G)
    NodeList = list(G.nodes())
    NodeList.sort()
    # setp 1
    curCyc = list()
    for ix in NodeList[:-2]:  # v1
        if NodeGirth[ix] == 0:
            continue
        curCyc.append(ix)
        for jx in NodeList[NodeList.index(ix) + 1 : -1]:  # v2
            if NodeGirth[jx] == 0:
                continue
            curCyc.append(jx)
            if G.has_edge(ix, jx):
                for kx in NodeList[NodeList.index(jx) + 1 :]:  # v3
                    if NodeGirth[kx] == 0:
                        continue
                    if G.has_edge(kx, ix):
                        curCyc.append(kx)
                        if G.has_edge(kx, jx):
                            SmallestCycles.add(tuple(curCyc))
                            for i in curCyc:
                                NodeGirth[i] = 3
                        curCyc.pop()
            curCyc.pop()
        curCyc.pop()
    # setp 2
    ResiNodeList = []  # Residual Node List
    for nod in NodeList:
        if NodeGirth[nod] == DEF_IMPOSSLEN:
            ResiNodeList.append(nod)
    if len(ResiNodeList) == 0:
        return
    else:
        visitedNodes = dict.fromkeys(ResiNodeList, set())
        for nod in ResiNodeList:
            if Coreness[nod] == 2 and NodeGirth[nod] < DEF_IMPOSSLEN:
                continue
            for nei in list(G.neighbors(nod)):
                if Coreness[nei] == 2 and NodeGirth[nei] < DEF_IMPOSSLEN:
                    continue
                if not nei in visitedNodes.keys() or not nod in visitedNodes[nei]:
                    visitedNodes[nod].add(nei)
                    if nei not in visitedNodes.keys():
                        visitedNodes[nei] = set([nod])
                    else:
                        visitedNodes[nei].add(nod)
                    if Coreness[nei] == 2 and NodeGirth[nei] < DEF_IMPOSSLEN:
                        continue
                    G.remove_edge(nod, nei)
                    if nx.has_path(G, nod, nei):
                        for path in my_all_shortest_paths(G, nod, nei):
                            lenPath = len(path)
                            path.sort()
                            SmallestCycles.add(tuple(path))
                            for i in path:
                                if NodeGirth[i] > lenPath:
                                    NodeGirth[i] = lenPath
                    G.add_edge(nod, nei)
    return SmallestCycles


def StatisticsAndCalculateIndicators(SmallestCycles):  #
    global NumSmallCycles
    NumSmallCycles = len(SmallestCycles)
    for cyc in SmallestCycles:
        lenCyc = len(cyc)
        CycLenDict[lenCyc] += 1
        for nod in cyc:
            SmallestCyclesOfNodes[nod].add(cyc)
    for objNode, SmaCycs in SmallestCyclesOfNodes.items():
        if len(SmaCycs) == 0:
            continue
        cycleNeighbors = set()
        NeiOccurTimes = {}
        for cyc in SmaCycs:
            for n in cyc:
                if n in NeiOccurTimes.keys():
                    NeiOccurTimes[n] += 1
                else:
                    NeiOccurTimes[n] = 1
            cycleNeighbors = cycleNeighbors.union(cyc)
        cycleNeighbors.remove(objNode)
        del NeiOccurTimes[objNode]
        sum = 0
        for nei in cycleNeighbors:
            sum += float(NeiOccurTimes[nei]) / len(SmallestCyclesOfNodes[nei])
        CycleRatio[objNode] = sum + 1


def cycle_ratio_centrality(G):
    """

    Parameters
    ----------
    G :   eg.Graph

    Returns
    -------
    cycle ratio centrality of each node in G : dict

    """
    cycles = getSmallestCycles(G)
    cycle_ratio = StatisticsAndCalculateIndicators(cycles)
    return cycle_ratio


def main():
    G = eg.Graph()
    G.add_edges([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 5), (2, 5)])
    print(G)
    res = cycle_ratio_centrality(G)
    print(res)


if __name__ == "__main__":
    main()