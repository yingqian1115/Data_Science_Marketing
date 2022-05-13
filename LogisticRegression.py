import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv") #pd.read_csv(./+檔案名)
df.shape #看資料有多少列和欄 (9134行# ,24欄)
df.head() #顯示前五筆資料
df["Engaged"] = df["Response"].apply(lambda x:0 if x=="No" else 1)
engagement_rate_df = pd.DataFrame(df.groupby("Engaged")["Response"].count()/df.shape[0]*100.0)
# print(engagement_rate_df.T) .T可以轉置pandas資料框 ->欄和行轉換
#response:14% no-response:86%                                                                             # aggfunc=len用來計數
#Sales Channel,Response的關係
engagement_by_sales_channel_df = pd.pivot_table(df,values="Response",index="Sales Channel",columns="Engaged",aggfunc=len).fillna(0.0)
engagement_by_sales_channel_df.columns = ["Not Engaged","Engaged"]                         # fillna(指定替換空值的方式)-->用0.0替換所有的空值
print(engagement_by_sales_channel_df)
engagement_by_sales_channel_df.plot(
    kind="pie",
    figsize=(15,7),
    startangle=45, # 字的角度(?
    subplots=True,
    autopct=lambda x : "%0.1f%%" %x
)

ax = df[["Engaged","Total Claim Amount"]].boxplot(
    by = "Engaged", #分群,
    showfliers = True, #設True會顯現離群值
    figsize = (7,5)
)
ax.set_xlabel("Engaged")
ax.set_ylabel("Total Claim Amount")
ax.set_title("Total Claim Amount Distributions by Engagements ")
plt.suptitle("") #把副標題拿掉
plt.show()


