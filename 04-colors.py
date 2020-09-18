from PIL import Image
from matplotlib import pyplot as plt

file = 'data/wave.jpg'

im = Image.open(file)

plt.imshow(im);

# https://github.com/obskyr/colorgram.py
# ! pip install colorgram.py

import colorgram

def rgb2hex(r, g, b):
    return f'#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}'

def hex2rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255. for i in (1, 3, 5)) # skip '#'

colors = 5
palette = colorgram.extract(file, colors)
rgbs = [color.rgb for color in palette]
hexcodes = [rgb2hex(c.r, c.g, c.b) for c in rgbs]

# grid design
# https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html

columns = colors
rows = columns + 1

figure = plt.figure(figsize=(8, 6), constrained_layout=False, dpi=100)
grid = plt.GridSpec(
    nrows=rows,
    ncols=columns,
    wspace=0,
    hspace=0.2,
    figure=figure
)

main = plt.subplot(grid[:rows-1, :columns])
axes = [plt.subplot(grid[rows-1, col]) for col in range(columns)]

for ax, hexcode in zip(axes, hexcodes):
    ax.set_facecolor(hexcode)
    mean_brightness = sum(hex2rgb(hexcode)) / 3
    text_color = "#ffffff" if mean_brightness < 0.5 else "#000000"
    ax.text(0.5, 0.5, hexcode, size=10, color=text_color, ha='center', va='center')

main.imshow(im, extent=[0,100,0,1], aspect='auto')
subplots = [main] + axes

for subplot in subplots:
    subplot.set_xticks([])
    subplot.set_yticks([])
    for spine in subplot.spines.values():
        spine.set_visible(False)

figure.suptitle("Wave", y=0.925)

# https://www.youtube.com/watch?v=6EcPEOpyApI
# https://www.reddit.com/r/pics/comments/iq0gph/one_day_difference_in_fort_collins_colorado/

import gif

@gif.frame
def plot(image_path, title, colors=5):
    im = Image.open(image_path)
    im = im.convert('P', colors=10)
    palette = colorgram.extract(image_path, colors)

    rgbs = [color.rgb for color in palette]
    hexcodes = [rgb2hex(c.r, c.g, c.b) for c in rgbs]
    columns = colors
    rows = columns + 1

    figure = plt.figure(figsize=(8, 6), constrained_layout=False)
    grid = plt.GridSpec(
        nrows=rows,
        ncols=columns,
        wspace=0,
        hspace=0.2,
        figure=figure
    )

    main = plt.subplot(grid[:rows-1, :columns])
    axes = [plt.subplot(grid[rows-1, col]) for col in range(columns)]

    for ax, hexcode in zip(axes, hexcodes):
        ax.set_facecolor(hexcode)
        mean_brightness = sum(hex2rgb(hexcode)) / 3
        text_color = "#ffffff" if mean_brightness <= 0.75 else "#000000"
        ax.text(0.5, 0.5, hexcode, size=10, color=text_color, ha='center', va='center')

    main.imshow(im, extent=[0,100,0,1], aspect='auto')
    subplots = [main] + axes

    for subplot in subplots:
        subplot.set_xticks([])
        subplot.set_yticks([])
        for spine in subplot.spines.values():
            spine.set_visible(False)

    figure.suptitle(title, y=0.925);

gif.options.matplotlib['dpi'] = 200

frames = []
files = ['before', 'during', 'after']
for file in files:
    frame = plot(f"data/{file}.png", title=f"Cameron Peak Fire: {file.capitalize()}")
    frames.append(frame)

gif.save(frames, 'output/colors.gif', duration=4, unit='s', between='startend')
