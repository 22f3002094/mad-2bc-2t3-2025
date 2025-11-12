from celery import shared_task
from time import sleep
@shared_task(name = "add_together", ignore_result=False)
def add_together(a: int, b: int) -> int:
    sleep(15)
    return a + b


