import pandas as pd
import networkx as nx
import igraph
import matplotlib.pyplot as plt

def stringFromUnicode(unicode):
    string = str(unicode.encode('ascii', 'replace'))
    string = string.strip()
    return string

def saveGML(G):
    """Saves the network in a gml format."""
    g = igraph.Graph(directed=True)
    g.add_vertices(G.nodes())
    for node in G.nodes():
        g.vs[node]["jogtar filename"] = G.node[node]["jogtar filename"]
        g.vs[node]["type of decision"] = G.node[node]["type of decision"]
        g.vs[node]["title"] = G.node[node]["title"]
        g.vs[node]["year"] = G.node[node]["year"]
        g.vs[node]["all participating judges"] = G.node[node]["all participating judges"]
        g.vs[node]["dissenting judges"] = G.node[node]["dissenting judges"]
        g.vs[node]["drafting judge"] = G.node[node]["drafting judge"]
    g.add_edges(G.edges())
    g.save("ABhatarozatok.gml")

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

    print G.number_of_nodes()
    print G.number_of_edges()

    nx.write_gml(G, 'ABhatarozatok.gml')
    # saveGML(G)
