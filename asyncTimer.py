import asyncio

class AsyncTimer:
    def __init__(self, interval: int, callback):
        self.interval = interval  # Интервал в секундах
        self.callback = callback  # Функция для выполнения
        self._task = None
        self._active = False

    async def _run(self):
        while self._active:
            await asyncio.sleep(self.interval)
            if self._active:  # Проверяем, не был ли остановлен таймер во время сна
                await self.callback()

    def start(self):
        if not self._active:
            self._active = True
            self._task = asyncio.create_task(self._run())

    def stop(self):
        if self._active:
            self._active = False
            if self._task:
                self._task.cancel()
                self._task = None

    def restart(self):
        self.stop()
        self.start()


async def my_callback():
    print("Таймер сработал!")

async def main():
    timer = AsyncTimer(interval=2, callback=my_callback)

    print("Запуск таймера на 2 секунды...")
    timer.start()

    await asyncio.sleep(7)  # Даем таймеру поработать ~3 раза

    print("Останавливаю таймер...")
    timer.stop()

    await asyncio.sleep(3)  # Проверим, что больше сообщений нет

    print("Перезапускаю таймер...")
    timer.restart()

    await asyncio.sleep(5)  # Даем таймеру снова поработать

    print("Финально останавливаю")
    timer.stop()


if __name__ == "__main__":
    asyncio.run(main())