"""
Головний модуль для системи Cimeika
Містить IntentObserver для автоматичного розгортання модулів
"""
import json
import logging
import os
from typing import List, Dict, Optional

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IntentObserver:
    """
    Клас для спостереження за намірами користувача та активації відповідних модулів.
    
    IntentObserver порівнює запити користувача з тригерами, визначеними в manifest.json,
    і пропонує активацію відповідних модулів.
    """
    
    def __init__(self, manifest_path: str = "manifest.json"):
        """
        Ініціалізує IntentObserver з вказаним шляхом до manifest.json
        
        Args:
            manifest_path: Шлях до файлу manifest.json
        """
        self.manifest_path = manifest_path
        self.modules = []
        self.load_manifest()
        logger.info("[ФАКТ] IntentObserver ініціалізовано")
    
    def load_manifest(self) -> None:
        """
        Завантажує конфігурацію модулів з manifest.json
        """
        try:
            if not os.path.exists(self.manifest_path):
                logger.error(f"[ФАКТ] Файл {self.manifest_path} не знайдено")
                return
            
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.modules = data.get('modules', [])
                logger.info(f"[ФАКТ] Завантажено {len(self.modules)} модулів з manifest.json")
        except json.JSONDecodeError as e:
            logger.error(f"[ФАКТ] Помилка парсингу JSON: {e}")
        except Exception as e:
            logger.error(f"[ФАКТ] Помилка завантаження manifest: {e}")
    
    def analyze_user_input(self, user_input: str) -> List[Dict]:
        """
        Аналізує вхідні дані користувача та шукає відповідні тригери
        
        Args:
            user_input: Текст запиту користувача
            
        Returns:
            Список модулів, які відповідають тригерам у запиті
        """
        logger.info(f"[МОДЕЛЬ] Аналізую запит користувача: '{user_input}'")
        
        matching_modules = []
        user_input_lower = user_input.lower()
        
        # Словник ключових слів для різних тригерів
        trigger_keywords = {
            "unstructured_text": ["нотатка", "записати", "текст", "замітка", "note", "write", "запис"],
            "event_planning": ["подія", "зустріч", "планування", "календар", "event", "meeting", "plan", "планувати", "захід"],
            "emotion_tracking": ["настрій", "емоція", "почуття", "mood", "emotion", "feeling", "почуваюся", "емоційний"],
            "creative_work": ["творчість", "малювати", "креативність", "creative", "draw", "art", "намалювати", "малюнок"]
        }
        
        for module in self.modules:
            trigger = module.get('trigger', '')
            keywords = trigger_keywords.get(trigger, [])
            
            # Перевіряємо, чи містить запит користувача ключові слова тригера
            if any(keyword in user_input_lower for keyword in keywords):
                matching_modules.append(module)
                logger.info(f"[МОДЕЛЬ] Знайдено відповідність: тригер '{trigger}' для модуля '{module.get('module')}'")
        
        return matching_modules
    
    def suggest_module_activation(self, user_input: str) -> Optional[str]:
        """
        Пропонує активацію модулів на основі аналізу запиту користувача
        
        Args:
            user_input: Текст запиту користувача
            
        Returns:
            Рядок з пропозицією активації модуля або None, якщо нічого не знайдено
        """
        matching_modules = self.analyze_user_input(user_input)
        
        if not matching_modules:
            logger.info("[НОВЕ] Тригери не спрацювали, модулі не активовані")
            return None
        
        suggestions = []
        for module in matching_modules:
            module_name = module.get('module', 'Unknown')
            description = module.get('description', 'Немає опису')
            action = module.get('action', 'activate')
            
            suggestion = (
                f"[НОВЕ] Виявлено необхідність активації модуля '{module_name}'.\n"
                f"Опис: {description}\n"
                f"Дія: {action}"
            )
            suggestions.append(suggestion)
            logger.info(f"[НОВЕ] Пропоную активацію модуля: {module_name}")
        
        return "\n\n".join(suggestions)
    
    def process_request(self, user_input: str) -> str:
        """
        Обробляє запит користувача та повертає відповідь системи
        
        Args:
            user_input: Текст запиту користувача
            
        Returns:
            Відповідь системи з пропозиціями активації модулів
        """
        logger.info(f"[ФАКТ] Отримано запит користувача: '{user_input}'")
        
        suggestion = self.suggest_module_activation(user_input)
        
        if suggestion:
            return suggestion
        else:
            return "[ФАКТ] Не знайдено відповідних модулів для вашого запиту."


def main():
    """
    Основна функція для демонстрації роботи IntentObserver
    """
    print("=== Система Cimeika - IntentObserver ===")
    print("Введіть 'exit' для виходу\n")
    
    # Створюємо observer
    observer = IntentObserver()
    
    # Приклади запитів для тестування
    example_queries = [
        "Мені потрібно записати важливу нотатку про зустріч",
        "Хочу запланувати подію на наступний тиждень",
        "Сьогодні я почуваюся щасливим",
        "Допоможи мені намалювати щось креативне"
    ]
    
    print("Приклади запитів для тестування:")
    for i, query in enumerate(example_queries, 1):
        print(f"{i}. {query}")
    print()
    
    # Інтерактивний режим
    while True:
        user_input = input("Ваш запит: ").strip()
        
        if user_input.lower() == 'exit':
            print("[ФАКТ] Завершення роботи IntentObserver")
            break
        
        if not user_input:
            continue
        
        response = observer.process_request(user_input)
        print(f"\n{response}\n")
        print("-" * 50)


if __name__ == "__main__":
    main()
