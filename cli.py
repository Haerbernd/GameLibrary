#
# ----- ONLY TEMPORARY -----
# Starts only html files at the moment

import webbrowser


def start_html(url: str) -> None:
    webbrowser.open_new(url)


if __name__ == '__main__':
    user_input: str = input()
    start_html(user_input)
