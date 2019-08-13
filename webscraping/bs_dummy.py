from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special</li>
        <li class="special">This list item is also special</li>
        <li>This list item is not special</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""


print('===================================================')
data = BeautifulSoup(html, 'html.parser')
print(data.find_all(class_='special'))
print(data.select('.special'))
print('===================================================')
print(data.find(id='first'))
print(data.select('#first')[0])
print('===================================================')
print(data.find(attrs={'data-example': 'yes'}))
print(data.select('[data-example]'))