"""Basic arithmetic calculator functions."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of ``a`` and ``b``.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Parameters
    ----------
    a : float
        The number to subtract from.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The difference between ``a`` and ``b``.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of ``a`` and ``b``.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second.

    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.

    Returns
    -------
    float
        The quotient of ``a`` divided by ``b``.

    Raises
    ------
    ZeroDivisionError
        If ``b`` is zero.
    """
    return a / b


if __name__ == "__main__":
    first_number = 10.0
    second_number = 5.0
    print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
    print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
    print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
    print(f"{first_number} / {second_number} = {divide(first_number, second_number)}")