from func_name import func_name

print("=== TEST 1: Happy Path ===")
# Используем метод, который точно работает — чтение списков (их на доске много)
result1 = func_name(
    {
        "board_url": BOARD_URL,
        "element": "lists",
        "method": "read",
        "key": API_KEY,
        "token": API_TOKEN,
    }
)
print(f"Status: {result1.get('status')}")
assert result1.get("status") == "success", f"Happy path failed: {result1}"
print("✅ Test 1 Passed")


print("\n=== TEST 2: Validation Error ===")
# Чтобы ГАРАНТИРОВАТЬ ошибку, передаем полностью битый URL
result2 = func_name(
    {
        "board_url": "https://trello.com",
        "element": "cards",
        "method": "read",
        "key": API_KEY,
        "token": API_TOKEN,
    }
)
print(f"Status: {result2.get('status')}")
print(f"Result (Error): {result2.get('result')}")
# Теперь статус ДОЛЖЕН быть error
assert result2.get("status") == "error", "Должна быть ошибка на кривой URL"
assert "error" in result2.get("result", {}), "В результате должно быть описание ошибки"
print("✅ Test 2 Passed")


print("\n=== TEST 3: Debug Mode ===")
# Проверяем работу с флагом debug. Используем тот же успешный запрос
result3 = func_name(
    {
        "board_url": BOARD_URL,
        "element": "lists",
        "method": "read",
        "key": API_KEY,
        "token": API_TOKEN,
        "debug": True,
    }
)
print(f"Status: {result3.get('status')}")
# Если здесь 'error', проверь вывод в консоли (трассировку), которую вывел debug
assert (
    result3.get("status") == "success"
), f"Debug mode failed. Error: {result3.get('result')}"
print("✅ Test 3 Passed")


print("\n=== TEST 4: Format Check ===")
# Проверяем наличие обязательных ключей
required_keys = ["result", "status"]
for key in required_keys:
    assert key in result1, f"Ответ должен содержать ключ '{key}'"

assert isinstance(result1["result"], dict), "Ключ 'result' должен быть словарем"
assert (
    "data" in result1["result"] or "error" in result1["result"]
), "В result должно быть data или error"
print("✅ Test 4 Passed")


print("\n=== Все тесты пройдены успешно ===")
