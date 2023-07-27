import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as mpt
from openpyxl.workbook import Workbook
from scipy import stats

df = pd.read_excel('sample-xls-file-for-testing.xls', 'Sheet1')
df.set_index('Segment', inplace=True)
'''
#relational_plot
sb.relplot('Units Sold', 'Profit', data=df, hue='Country', style='Segment')
sb.relplot('Units Sold', 'Profit', data=df, size='Unit Cost')
sb.relplot('Units Sold', 'Profit', data=df, kind='line',  ci=None)
sb.relplot('Units Sold', 'Profit', data=df, kind='line',  estimator=sum)
sb.relplot('Units Sold', 'Profit', data=df, kind='line', hue='Segment', style='Country')
sb.relplot('Units Sold', 'Profit', data=df, kind='line', hue='Segment', col='Country')
sb.relplot('Units Sold', 'Profit', data=df, kind='line', hue='Segment', col='Country', col_wrap=2)
sb.relplot('Units Sold', 'Profit', data=df, hue='Segment', col='Product', row='Country')

#categorial_plot
sb.catplot('Product', 'Profit', data=df)
sb.catplot('Product', 'Profit', data=df, jitter=False)
sb.catplot('Product', 'Profit', data=df.query('Discounts > 5000'), jitter=False)
sb.catplot('Product', 'Profit', data=df.query('Discounts > 5000'), kind="swarm")
sb.catplot('Profit', 'Product', data=df.query('Discounts > 5000'), kind="swarm")

#box_plot
sb.catplot(x='Country', y='Units Sold', data=df, kind="box")
sb.catplot(x='Country', y='Units Sold', data=df, kind="box", hue="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="box", row="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="box", col="Product",col_wrap=2)

#violn
sb.catplot(x='Country', y='Units Sold', data=df, kind="violin")
sb.catplot(x='Country', y='Units Sold', data=df, kind="violin", hue="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="violin", row="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="violin", col="Product",col_wrap=2)
sb.catplot(x='Country', y='Units Sold', data=df, kind="violin", hue="Product", inner='stick')

#bar_plot
sb.catplot(x='Country', y='Units Sold', data=df, kind="bar")
sb.catplot(x='Country', y='Units Sold', data=df, kind="bar", hue="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="bar", row="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="bar", col="Product",col_wrap=2)

#point_plot
sb.catplot(x='Country', y='Units Sold', data=df, kind="point")
sb.catplot(x='Country', y='Units Sold', data=df, kind="point", row="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="point", hue="Product")
sb.catplot(x='Country', y='Units Sold', data=df, kind="point", col="Product",col_wrap=2)

#distribution_plot
sb.distplot(df.Profit)
sb.distplot(df.Profit, kde=False)
sb.distplot(df.Profit, hist=False)
sb.distplot(df.Profit, hist=False, rug=True)
sb.distplot(df.Profit, rug=True, bins=100)
sb.distplot(df.Profit[(df.Product == 'Montana') & (df.Country == 'Mexico')],kde=False, rug=True, bins=100)

#kernal_density_plot
sb.kdeplot(df.Profit, bw=100)

#probability_distribution(gamma)
a=np.random.gamma(6,size=200)
sb.distplot(a)
sb.distplot(a, fit=stats.gamma)
b = np.random.beta(6, 6, size=200)
sb.distplot(b, fit=stats.beta)

#joint_plot
sb.jointplot('Country', 'Units Sold', data=df)
sb.jointplot('Units Sold', 'Profit', data=df, kind="hex")
sb.jointplot('Units Sold', 'Profit', data=df, kind="kde")
sb.jointplot('Units Sold', 'Profit', data=df, kind="scatter")
sb.jointplot('Units Sold', 'Profit', data=df, kind="resid")

#pair_plot
sb.pairplot(df)
sb.pairplot(df, hue='Product')

#heat map
sb.heatmap(df.corr(), annot=True)
'''
fig = mpt.figure()
sb.catplot(x='Country', y='Units_Sold', data=df, kind="point")
mpt.show()
sb.catplot(x='Country', y='Units_Sold', data=df, kind="point", row="Product")
mpt.show()
sb.catplot(x='Country', y='Units_Sold', data=df, kind="point", hue="Product")
mpt.show()
sb.catplot(x='Country', y='Units_Sold', data=df, kind="point", col="Product",
           col_wrap=2)
mpt.show()
sb.pairplot(df, hue='Product')
# mpt.savefig("plot11.png", dpi=400, bbox_inches="tight")
mpt.show()
