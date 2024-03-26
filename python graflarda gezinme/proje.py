import networkx as nx  

from collections import deque  

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 5, 6, 7, 9])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 9)])


def dfs(graph, baslangic, ziyaret_edilen=None, gezinme_sirasi=None):
    # Başlangıç değerleri kontrolü
    if ziyaret_edilen is None:
        ziyaret_edilen = set()
    if gezinme_sirasi is None:
        gezinme_sirasi = []

    ziyaret_edilen.add(baslangic)
    gezinme_sirasi.append(baslangic)

    for komsu in graph[baslangic]:
        if komsu not in ziyaret_edilen:
            dfs(graph, komsu, ziyaret_edilen, gezinme_sirasi)


    return gezinme_sirasi


def bfs(graph, baslangic):
 
    ziyaret_edilen = set()
    gezinme_sirasi = []
    kuyruk = deque([baslangic])


    while kuyruk:
        dugum = kuyruk.popleft()
        if dugum not in ziyaret_edilen:
            ziyaret_edilen.add(dugum)
            gezinme_sirasi.append(dugum)
            kuyruk.extend(set(graph[dugum]) - ziyaret_edilen)

    return gezinme_sirasi

dfs_sirasi = dfs(G, 1)
bfs_sirasi = bfs(G, 1)

print("DFS Gezinme Sırası:", dfs_sirasi)
print("BFS Gezinme Sırası:", bfs_sirasi)

aranan_deger = int(input("Listenin içinde aranacak değeri giriniz: "))

if aranan_deger in dfs_sirasi:
    print(f"{aranan_deger} DFS gezinme sırasında bulundu.")
else:
    print(f"{aranan_deger} DFS gezinme sırasında bulunamadı.")

if aranan_deger in bfs_sirasi:
    print(f"{aranan_deger} BFS gezinme sırasında bulundu.")
else:
    print(f"{aranan_deger} BFS gezinme sırasında bulunamadı.")
