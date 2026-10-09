def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    """
    Returns values clipped to the interpolated percentile bounds.
    """
    # Write code here
    n=len(values)
    k_l=(n-1)*lower_pct/100
    k_u=(n-1)*upper_pct/100

    q_l=values[int(k_l)] + (k_l-int(k_l))*(values[int(k_l) + 1 if k_l != int(k_l) else int(k_l)]-values[int(k_l)])
    q_u=values[int(k_u)] + (k_u-int(k_u))*(values[int(k_u) + 1 if k_u != int(k_u) else int(k_u)]-values[int(k_u)])
    alpha=-1;beta=n
    for i in range(len(values)):
        if q_l >values[i]:
            alpha=i
    for i in range(len(values)-1,-1,-1):
        if q_u <values[i]:
            beta=i  

    if alpha >-1:
        for i in range(alpha,-1,-1):
            values[i]=q_l


    if beta <n:
        for i in range(beta,n):
            values[i]=q_u

    return values
            
        

    