# -*- coding: utf8
import random
import sys
from datetime import datetime

from termcolor import colored 

TIMES = {
    "en": [
        (["preamble"], "It is"),
        (["exactly"], "exactly"),
        (["about"], "about"),
        (["m55", "m05", "m25", "m35"], "five"),
        (["m50", "m10"], "ten"),
        (["m45", "m15"], "a quarter"),
        (["m40", "m20"], "twenty"),
        (["m40", "m45", "m50", "m55", "m25"], "to"),
        (["m35", "m05", "m10", "m15", "m20"], "past"),
        (["m30", "m25", "m35"], "half"),
        (["h13", "h01"], "one"),
        (["h14", "h02"], "two"),
        (["h15", "h03"], "three"),
        (["h16", "h04"], "four"),
        (["h17", "h05"], "five"),
        (["h18", "h06"], "six"),
        (["h19", "h07"], "seven"),
        (["h20", "h08"], "eight"),
        (["h21", "h09"], "nine"),
        (["h22", "h10"], "ten"),
        (["h23", "h11"], "eleven"),
        (["h00", "h12"], "twelve"),
        (["m00"], "o' clock"),
        (["h12", "h21", "h22", "h23", "h00", "h01", "h02", "h03"], "at"),
        (
            [
                "h13",
                "h14",
                "h15",
                "h16",
                "h17",
                "h18",
                "h19" "h20",
                "h04",
                "h05",
                "h06",
                "h07",
                "h08",
                "h09",
                "h10",
                "h11",
            ],
            "in the",
        ),
        (["h21", "h22", "h23", "h00", "h01", "h02", "h03"], "night"),
        (["h04", "h05", "h06", "h07", "h08", "h09", "h10", "h11"], "morning"),
        (["h12"], "noon"),
        (["h13", "h14", "h15", "h16", "h17"], "afternoon"),
        (["h18", "h19", "h20"], "evening"),
    ],
    "ch": [
        (["preamble"], "Es isch"),
        (["exactly"], "genau"),
        (["about"], "öppe"),
        (["m55", "m05", "m25", "m35"], "füf"),
        (["m50", "m10"], "zää"),
        (["m45", "m15"], "viertu"),
        (["m40", "m20"], "zwänzg"),
        (["m40", "m45", "m50", "m55", "m25"], "vor"),
        (["m35", "m05", "m10", "m15", "m20"], "ab"),
        (["m30", "m25", "m35"], "haubi"),
        (["h13", "h01"], "eis"),
        (["h14", "h02"], "zwöi"),
        (["h15", "h03"], "drüü"),
        (["h16", "h04"], "vieri"),
        (["h17", "h05"], "füfi"),
        (["h18", "h06"], "sächsi"),
        (["h19", "h07"], "sibni"),
        (["h20", "h08"], "achti"),
        (["h21", "h09"], "nüni"),
        (["h22", "h10"], "zähni"),
        (["h23", "h11"], "eufi"),
        (["h00", "h12"], "zwöufi"),
        (
            [
                "h05",
                "h06",
                "h07",
                "h08",
                "h09",
                "h10",
                "h11",
                "h12",
                "h13",
                "h14",
                "h15",
                "h16",
                "h17",
                "h18",
                "h19",
                "h20",
                "h21",
                "h22",
            ],
            "am",
        ),
        (["h23", "h00", "h01", "h02", "h03", "h04"], "ir"),
        (["h21", "h22", "h23", "h00", "h01", "h02", "h03"], "nacht"),
        (["h04", "h05", "h06", "h07", "h08", "h09", "h10", "h11"], "morge"),
        (["h12"], "mittag"),
        (["h13", "h14", "h15", "h16", "h17"], "nami"),
        (["h18", "h19", "h20"], "aabe"),
    ],
}


def showtime():

    date = datetime.now()
    minutes = round(date.minute / 5) * 5
    precision = "exactly" if date.minute == minutes else "about"
    str_minutes = f"m{minutes:02}"
    hours = (date.hour if minutes < 25 else date.hour + 1) % 24
    str_hours = f"h{hours:02}"
    langs = [lang for lang in TIMES if lang in sys.argv[1:]]
    lang = langs[0] if langs else "en"

    actives = set([str_hours, str_minutes, "preamble", precision])

    on_choices = [
        lambda s: colored(s, 'yellow', attrs=['bold']),
        lambda s: colored(s, 'cyan', attrs=['bold']),
        lambda s: colored(s, 'white', attrs=['bold']),
        lambda s: colored(s, 'green', attrs=['bold']),
            
    ]

    off_color = lambda s: '' if 'nofill' in sys.argv else colored(s, 'blue', attrs=['dark']) 

    newl = "" if 'nofill' in sys.argv else "\n"

    written = 0
    for activation, string in TIMES[lang]:
        is_active = set(activation).intersection(actives)
        color = random.choice(on_choices) if is_active else off_color

        sys.stdout.write(color(string+" "))
        written += len(string)
        if written > 25:
            sys.stdout.write(newl)
            written = 0

    sys.stdout.write("\n")
    sys.stdout.flush()


if __name__ == "__main__":
    showtime()
