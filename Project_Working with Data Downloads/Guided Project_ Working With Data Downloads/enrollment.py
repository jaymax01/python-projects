import pandas as pd
data01 = pd.read_csv("data/CRDC2013_14.csv")
data01["total_enrollment"] = data01["TOT_ENR_M"] + data01["TOT_ENR_F"]
columns = ["SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F" ,"SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M" , "SCH_ENR_HP_F" , "SCH_ENR_BL_M" , "SCH_ENR_BL_F" , "SCH_ENR_WH_M" , "SCH_ENR_WH_F" , "SCH_ENR_TR_M", "SCH_ENR_TR_F"]
enr_gen_ra = data01[columns]
print(enr_gen_ra)
sums_en_gen_ra = enr_gen_ra.sum(axis=0)
print(sums_en_gen_ra)
all_enrollment = data01["total_enrollment"].sum()
print()
print(all_enrollment)
per_enr_ra_gen = sums_en_gen_ra / all_enrollment
print()
print(per_enr_ra_gen)
