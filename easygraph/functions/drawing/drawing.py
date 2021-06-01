import easygraph as eg 
import matplotlib.pyplot as plt
import numpy as np
import random

__all__=[
    "draw_SHS_center",
    "draw_SHS_center_kk",
    "draw_kamada_kawai"
]

def draw_SHS_center(G,SHS,rate=1):
    """
    Draw the graph whose the SH Spanners are in the center, with random layout.

    Parameters
    ----------
    G : graph
        A easygraph graph.

    SHS : list
        The SH Spanners in graph G.

    rate : float
       The proportion of visible points and edges to the total 

    Returns
    -------
    graph : network
        the graph whose the SH Spanners are in the center.
    """
    pos=eg.random_position(G)
    center=np.zeros((len(SHS),2),float) 
    node=np.zeros((len(pos),2),float)
    m,n=0,0
    if rate==1:
        for i in pos:
            if i in SHS:
                node[m][0]=0.5+(-1)**random.randint(1,2)*pos[i][0]/5
                node[m][1]=0.5+(-1)**random.randint(1,2)*pos[i][1]/5
                center[n][0]=node[m][0]
                center[n][1]=node[m][1]
                pos[i][0]=node[m][0]
                pos[i][1]=node[m][1]
                m+=1
                n+=1
            else:
                node[m][0]=pos[i][0]
                node[m][1]=pos[i][1]
                m+=1
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        plt.scatter(center[:,0], center[:,1], marker = '*', color = 'r', s=20)
        k=0
        for i in pos:
            plt.text(pos[i][0], pos[i][1], i,
            fontsize=5,
            verticalalignment="top",
            horizontalalignment="right")
            k+=1
        for i in G.edges:
            p1=[pos[i[0]][0],pos[i[1]][0]]
            p2=[pos[i[0]][1],pos[i[1]][1]]
            plt.plot(p1,p2, 'k--',alpha=0.3) 
        plt.show()
    else:
        degree=G.degree()
        sorted_degree=sorted(degree.items(), key=lambda d: d[1],reverse=True)
        l=int(rate*len(G))
        s=[]
        for i in sorted_degree:
            if len(s)<l:
                s.append(i[0])
        for i in pos:
            if i in SHS and i in s:
                node[m][0]=0.5+(-1)**random.randint(1,2)*pos[i][0]/5
                node[m][1]=0.5+(-1)**random.randint(1,2)*pos[i][1]/5
                center[n][0]=node[m][0]
                center[n][1]=node[m][1]
                pos[i][0]=node[m][0]
                pos[i][1]=node[m][1]
                m+=1
                n+=1
            elif i in s:
                node[m][0]=pos[i][0]
                node[m][1]=pos[i][1]
                m+=1         
        node=node[0:m,:]
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        center=center[0:n,:]
        plt.scatter(center[:,0], center[:,1], marker = '*', color = 'r', s=20)
        k=0
        for i in pos:
            if i in s:
                plt.text(pos[i][0], pos[i][1], i,
                fontsize=5,
                verticalalignment="top",
                horizontalalignment="right")
                k+=1
        for i in G.edges:
            (u,v,t)=i
            if u in s and v in s:
                p1=[pos[i[0]][0],pos[i[1]][0]]
                p2=[pos[i[0]][1],pos[i[1]][1]]
                plt.plot(p1,p2, 'k--',alpha=0.3) 
        plt.show()
    return

def draw_SHS_center_kk(G,SHS,rate=1):
    """
    Draw the graph whose the SH Spanners are in the center, with a Kamada-Kawai force-directed layout.

    Parameters
    ----------
    G : graph
        A easygraph graph.

    SHS : list
        The SH Spanners in graph G.

    rate : float
       The proportion of visible points and edges to the total 

    Returns
    -------
    graph : network
        the graph whose the SH Spanners are in the center.
    """
    pos=eg.kamada_kawai_layout(G)
    center=np.zeros((len(SHS),2),float) 
    node=np.zeros((len(pos),2),float)
    m,n=0,0
    if rate==1:
        for i in pos:
            if i in SHS:
                node[m][0]=pos[i][0]/5
                node[m][1]=pos[i][1]/5
                center[n][0]=node[m][0]
                center[n][1]=node[m][1]
                pos[i][0]=node[m][0]
                pos[i][1]=node[m][1]
                m+=1
                n+=1
            else:
                node[m][0]=pos[i][0]
                node[m][1]=pos[i][1]
                m+=1
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        plt.scatter(center[:,0], center[:,1], marker = '*', color = 'r', s=20)
        k=0
        for i in pos:
            plt.text(pos[i][0], pos[i][1], i,
            fontsize=5,
            verticalalignment="top",
            horizontalalignment="right")
            k+=1
        for i in G.edges:
            p1=[pos[i[0]][0],pos[i[1]][0]]
            p2=[pos[i[0]][1],pos[i[1]][1]]
            plt.plot(p1,p2, 'k--',alpha=0.3) 
        plt.show()
    else:
        degree=G.degree()
        sorted_degree=sorted(degree.items(), key=lambda d: d[1],reverse=True)
        l=int(rate*len(G))
        s=[]
        for i in sorted_degree:
            if len(s)<l:
                s.append(i[0])
        for i in pos:
            if i in SHS and i in s:
                node[m][0]=pos[i][0]/5
                node[m][1]=pos[i][1]/5
                center[n][0]=node[m][0]
                center[n][1]=node[m][1]
                pos[i][0]=node[m][0]
                pos[i][1]=node[m][1]
                m+=1
                n+=1
            elif i in s:
                node[m][0]=pos[i][0]
                node[m][1]=pos[i][1]
                m+=1
        node=node[0:m,:]
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        center=center[0:n,:]
        plt.scatter(center[:,0], center[:,1], marker = '*', color = 'r', s=20)
        k=0
        for i in pos:
            if i in s:
                plt.text(pos[i][0], pos[i][1], i,
                fontsize=5,
                verticalalignment="top",
                horizontalalignment="right")
                k+=1
        for i in G.edges:
            (u,v,t)=i
            if u in s and v in s:
                p1=[pos[i[0]][0],pos[i[1]][0]]
                p2=[pos[i[0]][1],pos[i[1]][1]]
                plt.plot(p1,p2, 'k--',alpha=0.3) 
        plt.show()
    return

def draw_kamada_kawai(G,rate=1):
    """Draw the graph G with a Kamada-Kawai force-directed layout.

    Parameters
    ----------
    G : graph
       A networkx graph

    rate : float
       The proportion of visible points and edges to the total 

    """
    pos=eg.kamada_kawai_layout(G)
    node=np.zeros((len(pos),2),float)
    m,n=0,0
    if rate==1:
        for i in pos:
            node[m][0]=pos[i][0]
            node[m][1]=pos[i][1]
            m+=1
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        k=0
        for i in pos:
            plt.text(pos[i][0], pos[i][1], i,
            fontsize=5,
            verticalalignment="top",
            horizontalalignment="right")
            k+=1
        for i in G.edges:
            p1=[pos[i[0]][0],pos[i[1]][0]]
            p2=[pos[i[0]][1],pos[i[1]][1]]
            plt.plot(p1,p2, 'k--',alpha=0.3)
        plt.show()
    else:
        degree=G.degree()
        sorted_degree=sorted(degree.items(), key=lambda d: d[1],reverse=True)
        l=int(rate*len(G))
        s=[]
        for i in sorted_degree:
            if len(s)<l:
                s.append(i[0])
        for i in pos:
            if i in s:
                node[m][0]=pos[i][0]
                node[m][1]=pos[i][1]
                m+=1
        node=node[0:m,:]
        plt.scatter(node[:,0], node[:,1], marker = '.', color = 'b', s=10)
        k=0
        for i in pos:
            if i in s:
                plt.text(pos[i][0], pos[i][1], i,
                fontsize=5,
                verticalalignment="top",
                horizontalalignment="right")
                k+=1
        for i in G.edges:
            (u,v,t)=i
            if u in s and v in s:
                p1=[pos[i[0]][0],pos[i[1]][0]]
                p2=[pos[i[0]][1],pos[i[1]][1]]
                plt.plot(p1,p2, 'k--',alpha=0.3)
        plt.show()
    return