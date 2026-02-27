import matplotlib.pyplot as plt

def bar_chart(df, column):
    counts = df[column].value_counts()
    plt.figure()
    counts.plot(kind='bar')
    plt.title(f"{column} Distribution")
    plt.show()

def line_chart(df, x_col, y_col):
    plt.figure()
    plt.plot(df[x_col], df[y_col])
    plt.title(f"{y_col} over {x_col}")
    plt.show()
