import telebot
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Инициализация бота
bot = telebot.TeleBot('6164225985:AAH6qvB87eb3SNnF7Qjhf48p0T0HnLt_op4')

# Загрузка модели и токенизатора
model_path = "fine_tuned_model"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Переменная для хранения последнего сообщения пользователя
last_user_message = None

# Функция для генерации ответа с использованием модели
def generate_response(input_text):
  model.eval()  # inference
  input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
  with torch.no_grad():
      output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)
  response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
  return response

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, "Давай поболтаем. Напиши мне что-нибудь!")

# Обработчик текстовых сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
  global last_user_message
  user_input = message.text.lower().strip()

  # Если сообщение пользователя изменилось, генерируем ответ
  if user_input != last_user_message:
    last_user_message = user_input
    response = generate_response(user_input)

    print('выход модели: ', response)

    # Разделяем ответ на части по маркеру @@ВТОРОЙ@@
    parts = response.split('@@ВТОРОЙ@@')

    # По умолчанию бот отвечает, что не понимает запрос
    bot_response = "Извините, я вас не понял, пожалуйста сформулируйте свое предложение иначе("

    # Если есть вторая часть (после @@ВТОРОЙ@@), берем её
    if len(parts) > 1:
        bot_response = parts[1].strip()
    elif len(parts) == 1:
        bot_response = parts[0].strip()

    print("окончательный ответ бота: ", bot_response)
    bot.send_message(message.chat.id, bot_response) # отправляем результат пользователю

# Запуск бота
bot.polling(none_stop=True, interval=0)