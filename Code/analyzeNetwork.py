import networkx as nx
import matplotlib.pyplot as plt

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