from bokeh.plotting import figure, output_file, show, save, save,  ColumnDataSource
import pandas
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8

# Read in csv 
df = pandas.read_csv('cars.csv')

# car = df['Car']
# hp = df['Horsepower']

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# Cr lits
car_list = source.data['Car'].tolist()

# Add plot 
p = figure(
    y_range = car_list,
    plot_width = 800,
    plot_height = 600,
    title = 'Cars With Top Horsepower',
    x_axis_label = 'Horsepower',
    tools = 'pan, box_select, zoom_in, zoom_out, save, reset'
)

# Render glyph 
p.hbar(
    y = 'Car',
    right = 'Horsepower',
    left = 0,
    height =0.4,
    #color = 'orange',
    fill_color = factor_cmap(
        'Car',
        palette = Blues8,
        factors = car_list
    ),
    fill_alpha = 0.9,
    source = source
)


# Add Tooltips 

hover = HoverTool()
hover.tooltips = """
    <div>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>HP: </strong>@Horsepower</div>
    <div><img src="@Image" alt="" width="200" /></div>
    </div>
"""
p.add_tools(hover)
# Show results
#show(p)

# Save
save(p)