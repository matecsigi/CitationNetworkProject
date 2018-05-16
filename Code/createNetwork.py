import pandas as pd
import networkx as nx
import igraph
import matplotlib.pyplot as plt

def stringFromUnicode(unicode):
    string = str(unicode.encode('ascii', 'replace'))
    string = string.strip()
    return string

if __name__=='__main__':

    df = pd.read_excel('../Data/ABhatarozatok_v2.xlsx', sheet_name='ABhatarozatok')
           
    G = nx.DiGraph()
    for i in df.index:
        node = stringFromUnicode(df['number of decision'][i])
        G.add_node(node)
        G.node[node]['jogtarfilename'] = stringFromUnicode(df['jogtar filename'][i])
        G.node[node]['typeofdecision'] = stringFromUnicode(df['type of decision'][i])
        G.node[node]['title'] = stringFromUnicode(df['title'][i])
        if not pd.isnull(df['year '].iloc[i]):
            G.node[node]['year'] = int(df['year '][i])
        else:
            G.node[node]['year'] = 0
        if not pd.isnull(df['all participating judges'].iloc[i]):
            G.node[node]['allparticipatingjudges'] = stringFromUnicode(df['all participating judges'][i])
        else:
            G.node[node]['allparticipatingjudges'] = ""
        if not pd.isnull(df['dissenting judges'].iloc[i]):
            G.node[node]['dissentingjudges'] = stringFromUnicode(df['dissenting judges'][i])
        else:
            G.node[node]['dissentingjudges'] = ""
        if not pd.isnull(df['drafting judge'].iloc[i]):
            G.node[node]['draftingjudge'] = stringFromUnicode(df['drafting judge'][i])
        else:
            G.node[node]['draftingjudge'] = ""

    for i in df.index:
        if not pd.isnull(df['citations to other cc decisions'].iloc[i]):
           node = stringFromUnicode(df['number of decision'][i])
           neighbors = stringFromUnicode(df['citations to other cc decisions'][i])
           neighbors = neighbors.split(',')
           for neighbor in neighbors:
              neighbor = neighbor.strip()
              if G.has_node(neighbor) is True:
                G.add_edge(node, neighbor)

    print "ABhatarozatok graph, nodes:", G.number_of_nodes(), " edges:", G.number_of_edges()
    nx.write_gml(G, 'ABhatarozatok.gml')

    #G_reduced
    zeroDegreeCounter = 0
    removeNodes = []
    G_reduced = G.copy()
    for node in G_reduced.nodes():
        if (G_reduced.in_degree(node) == 0) and (G_reduced.out_degree(node) == 0):
            removeNodes.append(node)
            zeroDegreeCounter = zeroDegreeCounter+1
    G_reduced.remove_nodes_from(removeNodes)

    print "ABhatarozatok-reduced graph, nodes:", G_reduced.number_of_nodes(), " edges:", G_reduced.number_of_edges()
    nx.write_gml(G_reduced, 'ABhatarozatok-reduced.gml')

    # count = 0
    # for node in G.nodes():
    #     in_degree =  G.in_degree(node)
    #     out_degree =  G.out_degree(node)
    #     if in_degree == 0 and out_degree == 0:
    #         count = count+1
    # print "count=", count

    # saveGML(G)
