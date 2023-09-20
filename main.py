import random
import threading


def monte_carlo_single(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    pi_approximation = (inside_circle / num_points) * 4
    return pi_approximation


def monte_carlo_multi(num_points, num_threads):
    points_per_thread = num_points // num_threads
    inside_circle = [0] * num_threads
    threads = []

    def monte_carlo_thread(thread_num):
        local_inside_circle = 0
        for _ in range(points_per_thread):
            x, y = random.random(), random.random()
            if x ** 2 + y ** 2 <= 1:
                local_inside_circle += 1
        inside_circle[thread_num] = local_inside_circle

    for i in range(num_threads):
        thread = threading.Thread(target=monte_carlo_thread, args=(i,))
        threads.append(thread)
        thread.start()

    while any(thread.is_alive() for thread in threads):
        pass

    total_inside_circle = sum(inside_circle)
    pi_approximation = (total_inside_circle / num_points) * 4
    return pi_approximation


if __name__ == "__main__":
    num_points = int(input("Введіть кількість точок для обчислення: "))

    # Обчислення з одним потоком1
    pi_single_thread = monte_carlo_single(num_points)
    print(f"З одним потоком: Пі приблизно {pi_single_thread}")

    # Обчислення з використанням багатопотоковості
    num_threads = int(input("Введіть кількість потоків для обчислення: "))
    pi_multi_thread = monte_carlo_multi(num_points, num_threads)
    print(f"З використанням багатопотоковості ({num_threads} потоки): Пі приблизно {pi_multi_thread}")
