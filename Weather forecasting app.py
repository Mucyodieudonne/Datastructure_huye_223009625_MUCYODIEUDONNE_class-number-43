#includes libraries
from collections import deque
# variable declaration this is how to declare queue
recent_updates = deque()
#list declaration
forecast_history = []
#Stack declaration
undoing_forecast = []
def add_forecast(item):
    recent_updates.append(item)
    print(f"forecast added")
def processData():
    if recent_updates:
        recentItem = recent_updates.popleft()
        forecast_history.append(recentItem)
        undoing_forecast.append(recentItem)
        print(f"Data saved")
    else:
        print("no data found")
def undo_forecasted():
    if undoing_forecast:
        undoitem = undoing_forecast.pop()
        forecast_history.remove(undoitem)
        print(f"undo operation done Data:{undoitem}")
    else:
        print("no data to undo")
def view_history():
    print(f"History of forecast weather:{forecast_history}")

print("Weather forecasting App:\n\n")
print("1. Enter Z to undo \n\n")
print("2. Enter Q to Exist \n\n")
print("3. Enter V to  View Forecast History \n\n")


while 1:
    element = input("Enter weather forecast:\n")

    if element == 'Z':
        undo_forecasted()
    elif element == 'Q':
        break
    elif element == 'V':
        view_history()
    else:
        add_forecast("sunny day, date:20/3/2024")
        processData()





