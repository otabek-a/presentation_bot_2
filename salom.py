def data_help():
     doc = '''
# **Telegram Diagram Bot Documentation**

Welcome to the **Telegram Diagram Bot**! This bot helps you easily create and send different types of diagrams, including **pie charts**, **bar charts**, and **line graphs**. Here's how to use it:

## **Getting Started**

### **1. Start the Bot**

- To begin, send `/start` to the bot.
- The bot will reply with a set of buttons:  
  - **Pie chart**
  - **Bar chart**
  - **Line graph**

Choose one of these options to start creating your diagram.

---

## **Types of Diagrams**

### **Pie Chart 🍰**
To create a **pie chart**, follow these steps:

1. Type `pie/` followed by a list of **names and values**. Example:
   - `pie/Apple,10,Orange,20,Banana,30`
   - The bot will create a pie chart with the provided names and their respective values.
   
2. Alternatively, you can simply send a list of **values** after `pie/`:
   - `pie/10,20,30`
   - The bot will create a pie chart using those values and label them automatically.

---

### **Bar Chart 📊**
To create a **bar chart**, follow these steps:

1. Type `bar/` followed by a list of **names and values**. Example:
   - `bar/Apple,10,Orange,20,Banana,30`
   - The bot will create a bar chart with the provided names and their respective values.

2. Alternatively, send a list of **values** after `bar/`:
   - `bar/10,20,30`
   - The bot will create a bar chart with automatically generated labels.

---

### **Line Graph 📈**
To create a **line graph**, follow these steps:

1. Type `line/` followed by a list of **names and values**. Example:
   - `line/Jan,10,Feb,20,Mar,30`
   - The bot will create a line graph with the provided names and their respective values.

2. Alternatively, send a list of **values** after `line/`:
   - `line/10,20,30`
   - The bot will create a line graph using those values and label them automatically.

---

## **Bot Commands and Interactions**

- **/start** – Start the bot and get the main options (Pie chart, Bar chart, Line graph).
- **Pie chart** – Choose this option to create a pie chart.
- **Bar chart** – Choose this option to create a bar chart.
- **Line graph** – Choose this option to create a line graph.

---

## **How Does It Work?**
- The bot listens for the type of diagram you want (pie, bar, or line).
- It then processes the data you send after the diagram type and generates the appropriate chart.
- The generated chart is saved as an image and sent back to you.

---

## **Tips**

- Make sure to separate values with commas when entering them.
- You can use both **names and values** or just **values** for your charts.
- If you use names (e.g., Apple, Orange), the bot will label the diagram with those names.

---

### **Example Commands:**

- `pie/Apple,10,Orange,20,Banana,30`
- `bar/Apple,10,Orange,20,Banana,30`
- `line/10,20,30`

---

## **Help**

If you need further assistance or have any questions, feel free to ask! Just type `/help`, and the bot will guide you.

---

Hope this makes your experience with the Telegram Diagram Bot smooth and easy. Enjoy creating your charts, bro! 😎🎉
'''
     return doc