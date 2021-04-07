fin = open('README.md', 'rt').readlines()
fout = open('README.md', 'wt')


def replace_char(line, start): return line.replace(
    start, '').strip().replace(' ', '_').lower()


for line in fin:
    if line.startswith('## '):
        fout.write(line)
        parent_folder = replace_char(line, '## ')
    elif line.startswith('- '):
        fout.write(line)
        section_folder = replace_char(line, '- ')
    elif line.startswith('    - '):
        lesson_folder = replace_char(line, '    - ')
        fout.write(
            f"    - [{line[6:].strip()}](/{parent_folder}/{section_folder}/{lesson_folder})\n")
    else:
        fout.write(line)


fout.close()
