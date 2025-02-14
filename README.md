# DialogGPT_tg-bot  
Dialog Telegram Bot based on tinkoff-ai/ruDialoGPT-medium<br><br>  

Link to Colab (with a detailed model description): [Colab Notebook](https://colab.research.google.com/drive/13yY4eisgdwxYhLVZOpcMz-iy2R1xSn-O?usp=sharing) <br>  
Docker Image: ```docker pull anniborri/my_tg_bot``` <br>  

* **FT_DialogModel.ipynb** - notebook with code explanations (downloaded from Colab) <br>
* **bot.py** - code for the Telegram bot <br>
* **prepare_messages.py** - Telegram chat parser (```python prepare_messages.py result.json```) <br>

### Task Description  
Training a dialog language model, integrating it with a Telegram bot, and wrapping it in a Docker container.  

### Data Collection  
The initial data was generated manually in Telegram as a conversation between two users. This step was taken to ensure the model generates acceptable responses since tests with other open-source chats failed to achieve **satisfactory quality** (due to Colab’s limitations, training on a large dataset wasn’t possible).  
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/bdfa799a-708c-4af3-be75-059d3d99d71d)  

### Data Preparation  
I created a dictionary with two actors: user input (`@@FIRST@@`) and bot response (`@@SECOND@@`), which allowed me to prepare the training dataset for fine-tuning (more details in FT_DialogModel.ipynb).  
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/68afe01b-a4e2-4c2c-9b2e-e993518d6abd)  

### Hypothesis  
While working with the `reply_to_msg_id` column in the dataframe, I hypothesized that if the value of this column is `-1`, it indicates the start of a new conversation topic. All subsequent messages with this `msg_id` are replies to the original message. (This simplified hypothesis allowed for quick model training with **acceptable quality**) (see more in FT_DialogModel.ipynb).  

### Fine-tuning the Model  
For fine-tuning, I used the **Transformers** library and **PyTorch**. The base model used was **tinkoff-ai/ruDialoGPT-medium**. The model was fine-tuned on preprocessed data using the AdamW optimizer with a learning rate of `1e-5` and a batch size of 2 (due to Colab’s resource limitations, a small batch size was used). After training, the model was saved for use by the bot (more details in FT_DialogModel.ipynb).  

### Model Testing  
After training, I performed basic model testing by sending various text prompts and, upon receiving acceptable responses, proceeded to integration (more details in FT_DialogModel.ipynb).  

### Integration  
The model was integrated with a Telegram bot to generate real-time responses and wrapped in a Docker container (`bot.py`).  

**Note:** Model quality was assessed subjectively.  

### Conclusion  
Before fine-tuning, the Telegram bot couldn’t logically respond to basic prompts like "Hi", "How are you?", or "What are you doing?" (see example below).  
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/44f22845-ea6b-4385-b006-bb2f72407492)  

After fine-tuning, a significant improvement in responses was observed (more details in FT_DialogModel.ipynb).  

### **Model Improvement Directions:**  
1. **Expanding the Fine-tuning Dataset:**  
   The more diverse the conversation history, the better the model performance.  

2. **Nested Conversation History:**  
   In the current implementation, the conversation history consists of only one previous message. Using a deeper history (access to multiple previous messages) could improve training and make dialogues more coherent.  

3. **Training Hyperparameters:**  
   Parameters like `batch_size`, `learning_rate` (AdamW), and `num_epochs` play a crucial role in model training. Conducting more experiments could help find optimal values and achieve better results.  

### Example of Model Output:  
![image](https://github.com/Anya-wUw/DialogGPT_tg-bot/assets/48104500/30cce450-6250-4b0d-9e18-046b40d7b928)  

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
