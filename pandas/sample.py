import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", encoding='shift_jis', header=[1, 2], index_col=0)
print(df)
df.plot()

# グラフを画像ファイルに保存
plt.savefig("output.png")

# 画像ファイルを外部プログラムで表示
# 例: Windowsでは「explorer」としてファイルを開く
import subprocess
subprocess.run(["explorer", "output.png"])