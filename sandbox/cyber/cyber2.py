def check(str_: str) -> bool:
    open_ = 0
    close = 0

    if len(str_) < 2:
        return False

    for ch in str_:
        if ch == '(':
            open_ += 1
        if ch == ')':
            close += 1
        if close > open_:
            return False

    return open_ == close


assert check('qq(ww)eee') is True
assert check(')qwe(qwer') is False
assert check('qwq(e)e)r(t') is False
assert check('(qqw)(ewe(rwr') is False
assert check(')qwe(rew)(rewq') is False
assert check('wqwq)ewe)rr(e(wwe') is False
assert check('ewe(rew(ewe)rrw)we(rww)r') is True
assert check(')') is False
assert check('(') is False
assert check('()') is True
assert check(')(') is False
assert check('))((') is False
assert check('(()') is False
assert check('(())') is True
