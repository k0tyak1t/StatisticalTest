import scipy


def main():
    alpha_values = [.05, .02, .01]
    df_values = [9, 11, 10, 12]

    for df in df_values:
        for alpha in alpha_values:
            print_chi2(alpha, df)


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


if __name__ == '__main__':
    main()