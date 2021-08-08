This is a simple pygame addon to aid game developers in drawing static text in their games

How to use:
```
    from textlib import static_text
    from textlib.static_text import draw_text

    draw_text(display, loc, size, color, text)
    # Display = The display you want to render the text onto
    # Loc = The position of the text
    # Size = The font size of the text
    # Color = The color of the text in an rgb tuple i.e. (255, 255, 255)
    # Text = A string of your text. New lines can be marked with a "/"
```