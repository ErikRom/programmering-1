googol = 10**100

timmar = googol/60

timmar_under_dag = timmar % 24

if timmar_under_dag > 24:
    timmar_under_dag-24

print(timmar_under_dag)