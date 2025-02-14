# DialogGPT_tg-bot  

A Dialog Telegram Bot based on `tinkoff-ai/ruDialoGPT-medium`, trained and fine-tuned to generate human-like responses. This repository includes the code for fine-tuning the model, integrating it with a Telegram bot, and wrapping it in a Docker container for easy deployment.

---

## 📄 Description  

This project demonstrates how to build a dialog model using **ruDialoGPT-medium**, fine-tune it with custom Telegram chat data, and deploy it as a functional Telegram bot. The model generates contextual responses by predicting the next turn in a conversation.  

**Fine-tuning was done with a custom dataset**, representing dialogues between two actors: the user (`@@FIRST@@`) and the bot (`@@SECOND@@`), which improved the model's performance in generating relevant responses.

---

## 🔧 Features  
- Fine-tuned `tinkoff-ai/ruDialoGPT-medium` for personalized dialog generation.  
- Real-time Telegram bot integration (`bot.py`).  
- Docker container for simplified deployment.  
- Preprocessing of Telegram chat data (`prepare_messages.py`).  
- Code explanation and training details in `FT_DialogModel.ipynb`.  

---

## 📁 File Structure  

- **FT_DialogModel.ipynb**: Jupyter notebook with detailed code explanations for model fine-tuning and testing.  
- **bot.py**: Python script to integrate the fine-tuned model with Telegram's Bot API.  
- **prepare_messages.py**: Script for parsing Telegram chat data and preparing it for training (`python prepare_messages.py result.json`).  

---

## 🚀 Fine-tuning Process  

The fine-tuning was done using **Transformers** and **PyTorch** libraries. The base model, `tinkoff-ai/ruDialoGPT-medium`, was trained on manually created Telegram chat data to generate more coherent responses. Key steps:  

1. **Preprocessing**: Data was preprocessed into user-bot pairs.  
2. **Fine-tuning**: The model was fine-tuned using the AdamW optimizer (`learning_rate = 1e-5`, batch size = 2).  
3. **Testing**: The model's responses were evaluated on various text prompts, showing significant improvements after fine-tuning.  

---

## 🛠️ Requirements  

- Python 3.7+  
- PyTorch  
- Transformers  
- Telegram Bot API  
- Docker  

---

## 📦 Installation & Usage  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/DialogGPT_tg-bot.git
   cd DialogGPT_tg-bot
   ```

2. Build and run the Docker container:  
   ```bash
   docker pull anniborri/my_tg_bot
   docker run -it anniborri/my_tg_bot
   ```

3. Set up your Telegram bot token in `bot.py`.  
4. Run the bot:  
   ```bash
   python bot.py
   ```

---

## 🔍 Example  

Before fine-tuning:  
The bot couldn’t respond logically to basic prompts like **"Hello"**, **"How are you?"**, or **"What are you doing?"**.  

After fine-tuning:  
The responses became much more coherent and relevant, showing significant improvements.  

Example response:  
![Example Output](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/30cce450-6250-4b0d-9e18-046b40d7b928)

---

## 📈 Model Improvements  

1. **Expand the Dataset**: Use more diverse conversation datasets for better response quality.  
2. **Include Nested Conversation History**: Enable the bot to access multiple previous messages for context.  
3. **Optimize Training Hyperparameters**: Experiment with different batch sizes, learning rates, and epochs for improved results.  

<br><hr><br>
(Russian Translation)
# DialogGPT_tg-bot
Dialog Telegram Bot based on tinkoff-ai/ruDialoGPT-medium<br><br>
  
Ссылка на Colab (с подробным описанием модели): https://colab.research.google.com/drive/13yY4eisgdwxYhLVZOpcMz-iy2R1xSn-O?usp=sharing<br>
Image Docker: ```docker pull anniborri/my_tg_bot``` <br>

* FT_DialogModel.ipynb - ноутбук с пояснениями к коду (скачен с коллаба) <br>
* bot.py - код для телеграмм-бота <br>
* prepare_messages.py - парсер телеграмм-чатов (```python prepare_messages.py result.json```)<br>

### Описание задачи
Обучение диалоговой языковой модели и интегрирование её с телеграм-ботом, а также оборачивание в докер.

### Загрузка данных
Исходные данные были сгенерированы вручную в телеграмме, в виде переписки между двумя пользователями. Этот шаг был выполнен, чтобы модель могла генерировать наиболее приемлемые ответы, так как тесты с другими открытыми чатами не дали приемлемого качества** модели (ограничения в колабе не дали обучить большой чат).
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/bdfa799a-708c-4af3-be75-059d3d99d71d)


### Подготовка данных
Я создала словарь, состоящий из двух актеров: ввода пользователя (@@ПЕРВЫЙ@@) и ответа бота (@@ВТОРОЙ@@), что позволило мне подготовить тренировочный датасет для файтьюнинга. (подробнее в FT_DialogModel.ipynb)
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/68afe01b-a4e2-4c2c-9b2e-e993518d6abd)
<br>
### Гипотеза
Работая с колонкой reply_to_msg_id в датафрейме, я предположила, что если значение этой колонки равно -1, это означает начало новой темы в переписке. Все последующие сообщения с этим msg_id будут ответами на исходное сообщение. (Упрощенная гипотеза позволила быстро обучить модель на приемлемом качестве**) (подробнее в FT_DialogModel.ipynb)

### Fine-tuning модели
Для файнтьюнинга я использовала библиотеку Transformers и PyTorch. В качестве базовой модели была взята tinkoff-ai/ruDialoGPT-medium. Модель файтьюнилась на предобработанных данных с использованием оптимизатора AdamW с learning rate 1e-5 и размером батча 2 (из-за ограниченных ресурсов колаба был взят маленький батч). Затем модель была сохранена для использования ботом. (подробнее в FT_DialogModel.ipynb)

### Тестирование модели
После обучения я провела базовое тестирование модели, отправив ей различные текстовые запросы и получив приемлемые ответы, приступила к интеграции. (подробнее в FT_DialogModel.ipynb)

### Интеграция
Модель была интегрирована с телеграм-ботом для генерации ответов в реальном времени и обернута в докер-контейнер. (bot.py)
<br><br>
качество** модели было оценено субъективно

## Заключение
До файтьюнинга Телеграмм-бот не мог ответить логично на базовые промты например "привет)", "как дела?" или "что делаешь?". (см. фото ниже) <br>
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/44f22845-ea6b-4385-b006-bb2f72407492)
<br>
После файтьюнинга было замечено значительное улучшение ответов. (подробнее в FT_DialogModel.ipynb)

**Векторы для улучшения модели:**
1. **Расширение датасета для fine-tuning:**
Чем больше разнообразных историй переписок, тем лучше.
2. **Вложенная структура истории переписок:**
В текущей реализации есть только одно предыдущее сообщение в истории переписки. Можно рассмотреть более глубокую историю, где бот будет иметь доступ к нескольким предыдущим сообщениям пользователя. Это может улучшить обучение и сделать диалоги более качественными.
3. **Гиперпараметры обучения:** (batch_size, learning rate (AdamW), num_epochs) играют важную роль в обучении модели. Проведя больше экспериментов, можно найти оптимальные параметры, тем самым добиться лучших результатов

Пример работы модели: <br>
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/30cce450-6250-4b0d-9e18-046b40d7b928)
