import networkx as nx
import matplotlib.pyplot as plt

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

def plotRichClub(G):
    try:
        rc = nx.rich_club_coefficient(G, normalized=True, Q=500)
        plt.plot(rc.keys(),rc.values())
        # plt.show()
        pdfName = "rich-club.pdf"
        plt.savefig(pdfName, format='pdf')
        plt.close()
    except:
        print "new try"
        plotRichClub(G)

def plotGraph(G):
    f = plt.figure()
    nx.draw(G, node_size=100, node_color="r", edge_color="b", width = 0.1, aplha=0)
    plt.draw()
    plt.show()
    f.savefig('graph.pdf')    

def plotDegreeDistribution(G):
    pass

if __name__=='__main__':
    
    print "Analyzing network ..."
