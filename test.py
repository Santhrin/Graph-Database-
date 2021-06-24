from svo import findSVOs, printDeps, nlp
from scrap import scrapping, process
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

sentences = scrapping('https://english.onlinekhabar.com/new-corruption-case-against-chudamani-sharma.html')
sents = process(sentences)

tokens = nlp(sents)
svos = findSVOs(tokens)
print(svos)

sub = []
vb = []
obj = []

for x in svos:
    sub.append(x[0])
    vb.append(x[1])
    try:
        obj.append(x[2])
    except:
        obj.append('')


print(sub)
print('------------'*20)
print(vb)
print('------------'*20)
print(obj)
print('------------'*20)

#created dataframe
kg_df = pd.DataFrame({'source':sub, 'target':obj, 'edge':vb})

# # create a directed-graph from a dataframe
G=nx.from_pandas_edgelist(kg_df, "source", "target", 
                          ['edge'], create_using=nx.MultiDiGraph())
print(G.edges(data=True))
plt.figure(figsize=(12,12))

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
# plt.show()

#find the specific graph from the edge
user_input = input("type anything from the edge:\t")

G=nx.from_pandas_edgelist(kg_df[kg_df['edge']==user_input], "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12,12))
pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
