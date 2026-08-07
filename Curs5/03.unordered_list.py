
unordered_list = '<li>Python was created by Guido van Rossum and first released in 1991</li>\n\t\t<li>Python uses indentation (whitespace) to define code blocks instead of braces</li>\n\t\t<li>It is named after Monty Python Flying Circus, not the snake</li>'


base_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8|>
    <meta name="viewport" content="width=device-width, initial-scale=1,0">
    <title>Document</title>
</head>
<body>
    <ul>
        {unordered_list}
    </ul>
</body>
</html>
"""

with open("unordered_list.html", "w") as file_writer:
    file_writer.write(base_html)