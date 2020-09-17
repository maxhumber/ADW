from PIL import Image
from matplotlib import pyplot as plt

file = 'during.png'

im = Image.open(file)
im.convert('P', colors=10)

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
    # bbox={'facecolor':'white','alpha':1,'edgecolor':'none','pad':1},

main.imshow(im, extent=[0,100,0,1], aspect='auto')
subplots = [main] + axes

for subplot in subplots:
    subplot.set_xticks([])
    subplot.set_yticks([])
    for spine in subplot.spines.values():
        spine.set_visible(False)

figure.suptitle("Before", y=0.925)

# https://www.youtube.com/watch?v=6EcPEOpyApI
# https://www.reddit.com/r/pics/comments/iq0gph/one_day_difference_in_fort_collins_colorado/

import gif

gif.options.matplotlib['dpi'] = 300

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


frames = []
files = ['before', 'during', 'after']
for file in files:
    frame = plot(f"{file}.png", title=f"Cameron Peak Fire: {file.capitalize()}")
    frames.append(frame)

##


frames[2]


frames[0].convert('P', colors=256//3, dither=1)
frames[0].quantize(colors=256//3, kmeans=50)


save(frames, "cameron_peak.gif", duration=3, unit='seconds', between='startend')

frames[2]
gif.save(frames, "cameron_peak.gif", duration=3, unit='seconds', between='startend')

def save(frames, path, duration=3, unit='seconds', between='startend', loop=True):
    if unit in ["ms", "milliseconds"]:
        pass
    elif unit in ["s", "seconds"]:
        duration *= 1000
    else:
        raise ValueError(unit)

    if between == "frames":
        pass
    elif between == "startend":
        duration /= len(frames)
    else:
        raise ValueError(between)

    kwargs = {}

    if loop:
        kwargs["loop"] = 0

    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=duration,
        disposal=1,
        interlace=False,
        include_color_table=False,
        **kwargs
    )



plot("before.png", title=None)
plot("during.png", title=None)
plot("after.png", title=None)



### old stuff

rows = 7
columns = 6
fig8 = plt.figure(constrained_layout=False)
grid = plt.GridSpec(nrows=6+1, ncols=6, wspace=0, hspace=0.2, figure=fig8)
image = plt.subplot(grid[:rows-1, :columns])

plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(False)

c1 = plt.subplot(grid[rows-1, 0])
c2 = plt.subplot(grid[rows-1, 1])
c3 = plt.subplot(grid[rows-1, 2])
c4 = plt.subplot(grid[rows-1, 3])
c5 = plt.subplot(grid[rows-1, 4])
c6 = plt.subplot(grid[rows-1, 5])




#
