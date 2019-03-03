from bokeh.plotting import figure, output_file, show
import pandas

# Read in csv 
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']

output_file('index.html')

# Add plot 
p = figure(
    y_range = car,
    plot_width = 800,
    plot_height = 600,
    title = 'Cars With Top Horsepower',
    x_axis_label = 'Horsepower',
    tools = ''
)

# Render glyph 
p.hbar(
    y = car,
    right = hp,
    left = 0,
    height =0.4,
    color = 'orange',
    fill_alpha = 0.5 
)

# Show results
show(p)