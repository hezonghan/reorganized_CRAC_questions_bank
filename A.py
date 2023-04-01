
import os

# http://82.157.138.16:8091/CRAC/crac/pages/list_files.html
src_filepath = '../TXT题库包(v20211022)所有题目正确答案均为A选项/TXT题库包(v20211022)所有题目正确答案均为A选项/A类题库(v20211022).txt'
figures_path = '../TXT题库包(v20211022)所有题目正确答案均为A选项/TXT题库包(v20211022)所有题目正确答案均为A选项/总题库附图(v20211022)/'
out_filepath = './output.tex'

src_f = open(src_filepath, 'r')
src_lines = src_f.readlines()
src_f.close()

figures_list = os.listdir(figures_path)
print(figures_list)


def problems():
    counter = 0
    line_id = 0
    while line_id < len(src_lines):
        print('started line {}'.format(line_id+1))

        I = src_lines[line_id]
        assert I.startswith('[I]')
        line_id += 1

        Q = src_lines[line_id]
        assert Q.startswith('[Q]')
        line_id += 1

        A = src_lines[line_id]
        assert A.startswith('[A]')
        line_id += 1

        B = src_lines[line_id]
        assert B.startswith('[B]')
        line_id += 1

        C = src_lines[line_id]
        assert C.startswith('[C]')
        line_id += 1

        D = src_lines[line_id]
        assert D.startswith('[D]')
        line_id += 1

        P = src_lines[line_id]
        # print('[{}]'.format(P))
        assert P == '[P]\n'
        line_id += 1

        EMPTY = src_lines[line_id]
        assert EMPTY == '\n'
        line_id += 1

        counter += 1
        yield counter, I[3:-1], Q[3:-1], A[3:-1], B[3:-1], C[3:-1], D[3:-1]


out_f = open(out_filepath, 'x', encoding='UTF-8')

out_f.write('''
\\documentclass[twocolumn]{ctexart}  % ctexart to enable Chinese.
\\usepackage[utf8]{inputenc}
\\usepackage[a4paper, margin=0.6in]{geometry}
\\usepackage{color}
\\usepackage[cmyk]{xcolor}

\\title{业余无线电台操作能力考核\\\\A类题库\\\\整理}
% \\author{}
% \\date{September 2022}

\\begin{document}

\\maketitle
''')


for counter, I, Q, A, B, C, D in problems():
    out_f.write('\n\n')
    out_f.write('\\noindent\\rule{0.5\\textwidth}{1pt}\n')

    out_f.write('\\heiti \\textbf{{({:03d}) {}}} \\songti {{\\color{{gray}} [{}] }}\n'.format(counter, Q, I))
    out_f.write('\\begin{itemize}\n')
    out_f.write('\t\\item  {}\n'.format(A))
    out_f.write('\t\\item  {}\n'.format(B))
    out_f.write('\t\\item  {}\n'.format(C))
    out_f.write('\t\\item  {}\n'.format(D))
    out_f.write('\\end{itemize}\n')

    if (I + '.jpg') in figures_list:
        out_f.write('''
\\begin{{figure}}[htb]
    \\centering
    \\includegraphics[width=.49\\textwidth]{{{}}}
    \\caption{{{}}}

    \\label{fig:{{}}}
\\end{{figure}}\n
'''.format(
            figures_path + I + '.jpg',
            '第{:03d}题（{}）附图'.format(counter, I),
            I,
        ))


out_f.write('\n\\end{document}\n')

out_f.close()
