from urllib.request import urlopen
import sys
import argparse

def get_bezos():
    url="https://www.forbes.com/profile/jeff-bezos/"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    index=html.find('<div class="profile-info__item-value">') + len('<div class="profile-info__item-value">')
    bezos = html[index+1:index+7]
    return bezos


parser = argparse.ArgumentParser()
parser.add_argument(
    '-t',
    '--trunclen',
    type=int,
    metavar='trunclen'
)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    metavar='custom format',
    dest='custom_format'
)
parser.add_argument(
    '-p',
    '--playpause',
    type=str,
    metavar='play-pause indicator',
    dest='play_pause'
)
parser.add_argument(
    '--font',
    type=str,
    metavar='the index of the font to use for the main label',
    dest='font'
)
parser.add_argument(
    '--playpause-font',
    type=str,
    metavar='the index of the font to use to display the playpause indicator',
    dest='play_pause_font'
)


args = parser.parse_args()

def fix_string(string):
    # corrects encoding for the python version used
    if sys.version_info.major == 3:
        return string
    else:
        return string.encode('utf-8')

# Default parameters
output = fix_string(u'{play_pause} {artist}: {song} {album}')
trunclen = 40
#play_pause = fix_string(u'\u25B6,\u23F8') # first character is play, second is paused
play_pause = 'playing,paused'
label_with_font = '%{{T{font}}}{label}%{{T-}}'
font = args.font
play_pause_font = args.play_pause_font

# parameters can be overwritten by args
if args.trunclen is not None:
    trunclen = args.trunclen
if args.custom_format is not None:
    output = args.custom_format
if args.play_pause is not None:
    play_pause = args.play_pause

try:
    bezos = get_bezos()
    # guillotine = get_guillotine()
    # climate = get_climate()

    if not bezos:
        print('')
    else:
        if font:
            bezos = label_with_font.format(font=font, label=bezos)

        print(output.format(bezos=bezos))

except Exception as e:
        print(e)