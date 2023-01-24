from django.http.request import HttpRequest
from django.http.response import HttpResponse


def homepage_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Домашня сторінка")


def greeting_view(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Greeting, {name}")


def progression_view(request: HttpRequest, start: int, count: int, step: int) -> HttpResponse:
    counter = 1
    numbers = ''

    while counter <= count:
        counter += 1
        numbers += ' ' + str(start)
        start += step

    return HttpResponse(numbers.lstrip(' '))


def fibo_view(request: HttpRequest, n: int) -> HttpResponse:
    if n == 0:
        return HttpResponse(0)

    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    return HttpResponse(fib2)
