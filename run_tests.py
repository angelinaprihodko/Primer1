"""
Модульное тестирование контейнера верификации маркеров аутентификации
Автор: Приходько А.Р.
Дата: 24.04.2026
"""

import os
import sys
import json
import base64
import time

from main import generate_token, verify_token, TOKEN_TTL

# Цвета для вывода в консоль
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

passed = 0
failed = 0

def run_test(name, func):
    global passed, failed
    try:
        func()
        print(f"  {GREEN}✓{RESET} {name}")
        passed += 1
    except AssertionError as e:
        print(f"  {RED}✗{RESET} {name}")
        print(f"    {RED}Ошибка: {e}{RESET}")
        failed += 1
    except Exception as e:
        print(f"  {YELLOW}⚠{RESET} {name}")
        print(f"    {YELLOW}Исключение: {e}{RESET}")
        failed += 1

# ============================================================
print(f"\n{BOLD}{CYAN}{'='*70}{RESET}")
print(f"{BOLD}{CYAN}  АВТОМАТИЗИРОВАННОЕ МОДУЛЬНОЕ ТЕСТИРОВАНИЕ{RESET}")
print(f"{BOLD}{CYAN}  Контейнер верификации маркеров аутентификации{RESET}")
print(f"{BOLD}{CYAN}{'='*70}{RESET}\n")

# ==================== НАСТРОЙКА ОКРУЖЕНИЯ ====================
print(f"{BOLD}1. НАСТРОЙКА ТЕСТОВОГО ОКРУЖЕНИЯ{RESET}")

os.environ["TOKEN_SECRET_KEY"] = "test_secret_key_123"
print(f"  • TOKEN_SECRET_KEY установлен: test_secret_key_123")
print(f"  • TOKEN_TTL: {TOKEN_TTL} секунд")
print(f"  • Тестовый пользователь: user_1, роль: analyst")

# ==================== ТЕСТЫ ГЕНЕРАЦИИ МАРКЕРА ====================
print(f"\n{BOLD}2. ТЕСТИРОВАНИЕ МОДУЛЯ ГЕНЕРАЦИИ МАРКЕРА{RESET}")
print(f"   Функция: generate_token()\n")

def check_structure():
    token, iat = generate_token("user_1", "analyst", offset=0)
    parts = token.split(".")
    assert len(parts) == 2, f"Ожидалось 2 части, получено {len(parts)}"
    assert len(parts[0]) > 0, "Полезная нагрузка пуста"
    assert len(parts[1]) > 0, "Подпись пуста"
    print(f"     • Структура маркера: payload.signature ✓")
    print(f"     • Полезная нагрузка (Base64): {parts[0][:30]}...")
    print(f"     • Подпись: {parts[1][:30]}...")

def check_payload_fields():
    token, iat = generate_token("user_1", "analyst", offset=0)
    payload_b64 = token.split(".")[0]
    padding = 4 - len(payload_b64) % 4
    if padding != 4:
        payload_b64 += "=" * padding
    payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
    assert payload["user_id"] == "user_1"
    assert payload["role"] == "analyst"
    assert "iat" in payload
    assert "exp" in payload
    print(f"     • Поля payload: user_id='{payload['user_id']}', role='{payload['role']}'")
    print(f"     • iat={payload['iat']}, exp={payload['exp']}")

def check_ttl():
    token, iat = generate_token("user_1", "analyst", offset=0)
    payload_b64 = token.split(".")[0]
    padding = 4 - len(payload_b64) % 4
    if padding != 4:
        payload_b64 += "=" * padding
    payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
    assert payload["exp"] - payload["iat"] == TOKEN_TTL
    print(f"     • TTL = {payload['exp']} - {payload['iat']} = {TOKEN_TTL} секунд")

def check_offset():
    token1, iat1 = generate_token("user_1", "analyst", offset=0)
    token2, iat2 = generate_token("user_1", "analyst", offset=-200)
    diff = abs(iat1 - iat2)
    assert 190 <= diff <= 210, f"Разница должна быть ~200, получено {diff}"
    print(f"     • Смещение offset=-200, разница iat = {diff} секунд")

def check_different_tokens():
    token1, _ = generate_token("user_1", "analyst", offset=0)
    time.sleep(1.5)
    token2, _ = generate_token("user_1", "analyst", offset=0)
    assert token1 != token2
    print(f"     • Маркер 1: {token1[:40]}...")
    print(f"     • Маркер 2: {token2[:40]}...")
    print(f"     • Маркеры различаются ✓")

run_test("Проверка структуры маркера (две части)", check_structure)
run_test("Проверка полей полезной нагрузки", check_payload_fields)
run_test("Проверка времени жизни маркера (TTL=600)", check_ttl)
run_test("Проверка влияния offset на время выпуска", check_offset)
run_test("Проверка уникальности маркеров", check_different_tokens)

# ==================== ТЕСТЫ ВЕРИФИКАЦИИ МАРКЕРА ====================
print(f"\n{BOLD}3. ТЕСТИРОВАНИЕ МОДУЛЯ ВЕРИФИКАЦИИ МАРКЕРА{RESET}")
print(f"   Функция: verify_token()\n")

def check_no_dot():
    result = verify_token("invalid_token_without_dot")
    assert result["valid"] is False
    assert result["reason"] == "Неверная структура маркера"
    print(f"     • Результат: причина = '{result['reason']}'")

def check_extra_dot():
    result = verify_token("part1.part2.part3")
    assert result["valid"] is False
    assert result["reason"] == "Неверная структура маркера"
    print(f"     • Результат: причина = '{result['reason']}'")

def check_bad_signature():
    token, _ = generate_token("user_1", "analyst", offset=0)
    parts = token.split(".")
    tampered = parts[0] + "." + parts[1][:-4] + "XXXX"
    result = verify_token(tampered)
    assert result["valid"] is False
    assert result["reason"] == "Подпись недействительна"
    print(f"     • Подпись изменена, результат: '{result['reason']}'")

def check_expired():
    token, _ = generate_token("user_1", "analyst", offset=-700)
    result = verify_token(token)
    assert result["valid"] is False
    assert result["reason"] == "Маркер просрочен"
    print(f"     • Маркер просрочен (offset=-700), результат: '{result['reason']}'")

def check_future():
    token, _ = generate_token("user_1", "analyst", offset=+100)
    result = verify_token(token)
    assert result["valid"] is False
    assert result["reason"] == "Время выпуска в будущем"
    print(f"     • Время выпуска в будущем (offset=+100), результат: '{result['reason']}'")

def check_valid():
    token, _ = generate_token("user_1", "analyst", offset=0)
    result = verify_token(token)
    assert result["valid"] is True
    assert result["reason"] == "Верифицирован"
    assert result["payload"] is not None
    print(f"     • Результат: '{result['reason']}'")
    print(f"     • Пользователь: {result['payload']['user_id']}, роль: {result['payload']['role']}")

def check_tampering():
    token, iat = generate_token("user_1", "analyst", offset=0)
    exp = iat + TOKEN_TTL
    forged = json.dumps(
        {"user_id": "user_1", "role": "admin", "iat": iat, "exp": exp},
        separators=(",", ":")
    ).encode()
    forged_b64 = base64.urlsafe_b64encode(forged).decode().rstrip("=")
    tampered = forged_b64 + "." + token.split(".")[1]
    result = verify_token(tampered)
    assert result["valid"] is False
    assert result["reason"] == "Подпись недействительна"
    print(f"     • Попытка подмены роли на 'admin' обнаружена: '{result['reason']}'")

run_test("Уровень 1: Отклонение маркера без разделителя", check_no_dot)
run_test("Уровень 1: Отклонение маркера с лишними частями", check_extra_dot)
run_test("Уровень 2: Отклонение маркера с неверной подписью", check_bad_signature)
run_test("Уровень 3: Отклонение просроченного маркера", check_expired)
run_test("Уровень 3: Отклонение маркера из будущего", check_future)
run_test("Все уровни: Успешная верификация легитимного маркера", check_valid)
run_test("Атака: Обнаружение подмены содержимого (повышение роли)", check_tampering)

# ==================== КОНФИГУРАЦИОННЫЕ ТЕСТЫ ====================
print(f"\n{BOLD}4. КОНФИГУРАЦИОННОЕ ТЕСТИРОВАНИЕ{RESET}\n")

def check_with_key():
    os.environ["TOKEN_SECRET_KEY"] = "test_secret_key_123"
    token, _ = generate_token("user_1", "analyst", offset=0)
    result = verify_token(token)
    assert result["valid"] is True
    print(f"     • Режим HMAC-SHA256: маркер верифицирован")

def check_without_key():
    if "TOKEN_SECRET_KEY" in os.environ:
        del os.environ["TOKEN_SECRET_KEY"]
    token, _ = generate_token("user_1", "analyst", offset=0)
    result = verify_token(token)
    assert result["valid"] is True
    print(f"     • Режим SHA-256 (без ключа): маркер верифицирован")
    os.environ["TOKEN_SECRET_KEY"] = "test_secret_key_123"

run_test("Конфигурация: работа с заданным секретным ключом", check_with_key)
run_test("Конфигурация: работа без секретного ключа (fallback SHA-256)", check_without_key)

# ==================== НЕГАТИВНЫЕ ТЕСТЫ ====================
print(f"\n{BOLD}5. НЕГАТИВНОЕ ТЕСТИРОВАНИЕ{RESET}\n")

def check_empty():
    result = verify_token("")
    assert result["valid"] is False
    print(f"     • Пустая строка: '{result['reason']}'")

def check_long():
    long_str = "A" * 5000 + "." + "B" * 5000
    result = verify_token(long_str)
    assert result["valid"] is False
    print(f"     • Строка 10000 символов: '{result['reason']}' (без зависания)")

run_test("Негативный тест: пустая строка на входе", check_empty)
run_test("Негативный тест: строка из 10000 символов", check_long)

# ==================== ИТОГИ ====================
print(f"\n{BOLD}{CYAN}{'='*70}{RESET}")
print(f"{BOLD}{CYAN}  РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ{RESET}")
print(f"{BOLD}{CYAN}{'='*70}{RESET}\n")

total = passed + failed
print(f"  Всего тестов:       {BOLD}{total}{RESET}")
print(f"  Успешно пройдено:   {GREEN}{BOLD}{passed}{RESET}")
print(f"  Провалено:          {RED}{BOLD}{failed}{RESET}")

if failed == 0:
    print(f"\n  {GREEN}{BOLD}✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО{RESET}")
    print(f"  {GREEN}Контейнер верификации маркеров аутентификации{RESET}")
    print(f"  {GREEN}работает корректно во всех проверенных сценариях.{RESET}")
else:
    print(f"\n  {RED}{BOLD}✗ ОБНАРУЖЕНЫ ПРОБЛЕМЫ (тестов провалено: {failed}){RESET}")

print(f"\n{BOLD}{CYAN}{'='*70}{RESET}\n")