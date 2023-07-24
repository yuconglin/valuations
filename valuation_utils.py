import numpy as np

def _sum(*, initial_value, ratio, number):
    if ratio == 1.0:
        return initial_value * number
    return initial_value * ratio * (1.0 - ratio ** number) / (1.0 - ratio)

def dcf_value(*, starting_free_cash_flow, initial_year_number, initial_growth_rate, later_growth_rate, permanent_growth_rate, discount_rate, cash_and_equivalents, total_debt,  outstanding_shares):
    g0 = initial_growth_rate
    g1 = later_growth_rate
    g2 = permanent_growth_rate
    r = discount_rate 
    a0 = starting_free_cash_flow
    q0 = (1 + g0) / (1 + r)
    q1 = (1 + g1) / (1 + r)
    n = initial_year_number

    # predicted cash flow in first few years
    s0 = _sum(initial_value=a0, ratio=q0, number=n)
    # predicted cash flow in next phase
    s1 = _sum(initial_value=a0 * (q0 ** n), ratio=q1, number=n)
    # predicted cash flow forever after
    s2 = a0 * (q0 ** n) * (q1 ** n) * (1 + g2) / (r - g2)
    # total stock values
    s_total = s0 + s1 + s2 + cash_and_equivalents - total_debt
    # estimated stock price
    return s_total / outstanding_shares

def multiple_of_earnings_value(*, ebitda, outstanding_shares, multiple):
    return ebitda / outstanding_shares * multiple
