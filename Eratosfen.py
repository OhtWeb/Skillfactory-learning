def primes(n):
    """
    Генерирует простые числа до n с помощью алгоритма Решета Эратосфена.
    """
    if n < 2:
        return

    # Создаем список булевых значений (True — потенциально простое)
    sieve = [True] * (n + 1)

    for p in range(2, n + 1):
        if sieve[p]:
            yield p
            # "Вычеркиваем" все кратные числа, начиная с p*p
            for i in range(p * p, n + 1, p):
                sieve[i] = False
prime_generator = primes(89)
for prime in prime_generator:
   print(prime)