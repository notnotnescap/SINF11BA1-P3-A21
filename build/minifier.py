import python_minifier

with open('build/raw.py') as f:
    with open('main.py', 'w') as f2:
        f2.write(python_minifier.minify(f.read()))

print('Done!')