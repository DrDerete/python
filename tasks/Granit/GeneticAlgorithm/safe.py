import pandas as pd

def safe_as_excel(data_ind, ind_psl, index, population):
    ans = {
        "Номер особи в популяции": [i for i in range(len(data_ind))],
        "КП": [''.join(map(str, x)) for x in data_ind],
        "Значения PSL": [ind_psl[key] for key in ind_psl]
    }
    df = pd.DataFrame(ans)
    df.to_excel(str(index)+"_"+population +".xlsx", index=False)