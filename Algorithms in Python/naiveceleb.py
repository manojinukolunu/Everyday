def naive_celeb(G):
    n=len(G)
    for u in range(n):
        for v in range(n):
            if u==v:
                continue
            if G[u][v]:
                break
            if nor G[u][v]:
                break
        else:
            return u
    return None
