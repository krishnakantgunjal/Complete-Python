import time 
from plyer import notification 

while True :
    notification.notify(
    title='Drink Some Water',
    message='You need to Drink some Water !',
    app_name='My Python App',)
    time.sleep(60*60)