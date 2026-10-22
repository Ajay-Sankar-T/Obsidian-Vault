"""Make matplotlib mathtext happy: \frac12 -> \frac{1}{2}."""
import re, sys
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read()
    s2 = re.sub(r'\\frac(\d)(\d)', r'\\frac{\1}{\2}', s)
    open(p, 'w', encoding='utf-8').write(s2)
