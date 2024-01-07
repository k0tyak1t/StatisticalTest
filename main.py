import scipy
import numpy as np


def task3():
    alpha_values = [.05, .02, .01]
    df_values = [9, 11, 10, 12]

    for df in df_values:
        for alpha in alpha_values:
            print_chi2(alpha, df)

def task4_visual():
    alpha_values = np.linspace(0, .005, 20)
    df = 20
    tn = 3.049
    for alpha in alpha_values:
        t = get_t_critical(alpha, df)
        print(f'FOR {alpha: .4f}:   H0 {"is accepted" if h0_is_accepted(tn, t) else "is declined"}   t:   {t: .4f}')


def test():
    print(get_t_critical(.05, 20))


def get_chi_minus(alpha: float, df: int) -> float:
    return scipy.stats.chi2.ppf(alpha/2, df=df)


def get_chi_plus(alpha: float, df: int) -> float:
    return scipy.stats.chi2.ppf(1-alpha/2, df=df)


def print_chi2(alpha: float, df: int) -> None:
    print(f'FOR α = {alpha} (γ = {1-alpha} and df = {df})')
    print(f'χ+:  {get_chi_plus(alpha, df): .3f}')
    print(f'χ-:  {get_chi_minus(alpha, df): .3f}')


def get_param_from_keyboard() -> dict:
    alpha = float(input('Enter alpha:  '))
    df = int(input('Enter df:  '))
    return {'alpha': alpha, 'df': df}


def get_t_critical(alpha, df):
    return scipy.stats.t.ppf(q=1-alpha, df=df)


def h0_is_accepted(tn, t):
    return tn < t


if __name__ == '__main__':
    task4()
    #test()