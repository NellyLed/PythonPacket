from calc import add
from calc import dialogue
from calc import fibon
from calc import mul
from calc import sub
from calc import div
def test_add():
    a = 2
    b = 1
    c = 3
    d = 14
    assert add(a, b, c, d) == 20
def test_fibon():
    x = [x for x in fibon(15)]
    assert x == [1, 1, 2, 3, 5, 8, 13]
    assert len(x) == 7
def test_dialogue():
    name = 'ARMI'
    assert dialogue(name) == 'I purple your, ARMI'
def test_mul():
    k = 34
    w = 90
    q = 18
    l = 5
    assert mul(k, w, q, l) == 275400
def test_sub():
    e = 934
    f = 87
    g = 153
    assert sub(e, f, g) == 694
def test_div():
    p = 56
    m = 7
    assert div(p, m) == 8.0