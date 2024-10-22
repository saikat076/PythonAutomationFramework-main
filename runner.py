from behave.__main__ import main as behave_main
import sys

def run_behave():
    args = [
        '--tags', '@search',
        '--format',
        'behave_html_formatter:HTMLFormatter',
        '--out', 'features/reports/report.html',
        '--format', 'pretty',
        'features'
    ]

    sys.argv = ['behave'] + args
    behave_main()

if __name__ == "_main_":
    run_behave()