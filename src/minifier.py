import python_minifier

with open('src/source.py') as f:
    with open('main.py', 'w') as f2:
        f2.write('# le code original se trouve dans src/source.py\n')
        f2.write(python_minifier.minify(f.read(),
                                        remove_annotations=True,
                                        combine_imports=True,
                                        remove_pass=True,
                                        remove_literal_statements=True,
                                        hoist_literals=True,
                                        rename_locals=True,
                                        rename_globals=True,
                                        convert_posargs_to_args=True,
                                        preserve_shebang=True,
                                        remove_asserts=True,
                                        remove_explicit_return_none=True
                                        ))

print('Done!')