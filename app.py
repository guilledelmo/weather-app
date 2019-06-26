import tkinter
from tkinter import ttk

import data
import geolocation
#import icons

main_win = tkinter.Tk()
main_win.title("Weather")

json_response = {}
has_been_processed = False

def request_data():
    """Returns JSON response from API when given a user's location"""
    try:
        json_response = data.make_request(geolocation.get_lat(location_entry.get()), geolocation.get_long(location_entry.get()))
        print("Fetched weather for user entry: " + location_entry.get())
        render_weather_content(json_response)
    except AttributeError:
        print("Error - User entry: {}".format(location_entry.get()))
        # TODO: Add error message on app


def render_weather_content(api_response):
    if has_been_processed == True:
        # TODO: Delete all the content or just remove the frame and then run the code below
    # Weather icon component
    if api_response["currently"]["icon"] == "clear-day":
        weather_icon = tkinter.Label(information_frame, image=clear_day, bg="white")
    elif api_response["currently"]["icon"] == "clear-night":
        weather_icon = tkinter.Label(information_frame, image=clear_night, bg="white")
    elif api_response["currently"]["icon"] == "rain":
        weather_icon = tkinter.Label(information_frame, image=rain, bg="white")
    elif api_response["currently"]["icon"] == "snow":
        weather_icon = tkinter.Label(information_frame, image=snow, bg="white")
    elif api_response["currently"]["icon"] == "sleet":
        weather_icon = tkinter.Label(information_frame, image=sleet, bg="white")
    elif api_response["currently"]["icon"] == "wind":
        weather_icon = tkinter.Label(information_frame, image=wind, bg="white")
    elif api_response["currently"]["icon"] == "fog":
        weather_icon = tkinter.Label(information_frame, image=fog, bg="white")
    elif api_response["currently"]["icon"] == "cloudy":
        weather_icon = tkinter.Label(information_frame, image=cloudy, bg="white")
    elif api_response["currently"]["icon"] == "partly-cloudy-day":
        weather_icon = tkinter.Label(information_frame, image=partly_cloudy, bg="white")
    elif api_response["currently"]["icon"] == "partly-cloudy-night":
        weather_icon = tkinter.Label(information_frame, image=partly_cloudy_night, bg="white")
    weather_icon.grid(column=0, row=0, rowspan=2, padx=(15,0), pady=(15,0))
    
    # Temperature component
    temperature = tkinter.Label(information_frame, text=str(int(api_response["currently"]["temperature"])) + "°C", font=("Helvetica", 50, "bold"), bg="white")
    temperature.grid(column=1, columnspan=2, row=0, rowspan=2)
    # Summary component
    summary = tkinter.Label(information_frame, text=api_response["currently"]["summary"], bg="white", font=("Helvetica", 32))
    summary.grid(column=1, columnspan=2, row=2, pady=(5, 50))
    # Other info component
    other_info = tkinter.Label(information_frame, text="Wind: " + str(api_response["currently"]["windSpeed"]) + " km/h" + "\nHumidity: {}%".format(str(int(api_response["currently"]["humidity"] * 100))) + "\nCloud cover: {}%".format(str(int(api_response["currently"]["cloudCover"] * 100))), bg="white", font=("Helvetica", 10))
    other_info.grid(column=3, row=0, padx=(50,0), pady=(15,0))
    # Status
    #status = tkinter.Label(information_frame, text=api_response["timezone"] + "\n{},{}".format(str(api_response["latitude"]), str(api_response["longitude"])), font=("Helvetica", 4), bg="white")
    #status.grid(column=5, row=0, padx=(10, 0))
    status = tkinter.Label(information_frame, text="Data for: " + geolocation.get_info(location_entry.get()), bg="white", font=("Helvetica", 8))
    status.grid(column=1, row=3, columnspan=2)
    has_been_processed = True

# Main canvas creation
canvas = tkinter.Canvas(main_win, height=640, width=960)
canvas.pack()

# Background image
background_image = tkinter.PhotoImage(file=r'img\andreas-gucklhorn-285567-unsplash.png')
background_label = tkinter.Label(main_win, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Input frame content
input_frame = tkinter.Frame(main_win, bg="white", bd=5)
input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.07, anchor="n")
user_location = tkinter.StringVar()
location_entry = tkinter.Entry(input_frame, textvar=user_location, font=30)
location_entry.place(relwidth=0.65, relheight=1)
submit_button = tkinter.Button(input_frame, text="Find", command=request_data, font=5)
submit_button.place(relx=0.7, relwidth=0.3, relheight=1)

# Information frame content
information_frame = tkinter.Frame(main_win, bg="white")
information_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


imgicon = tkinter.PhotoImage(file=r"img\sun.ico") 
main_win.tk.call('wm', 'iconphoto', main_win._w, imgicon)

clear_day = tkinter.PhotoImage(file=r"img\sunny.png")
clear_night = tkinter.PhotoImage(file=r"img\moon.png")
rain = tkinter.PhotoImage(file=r"img\rain.png")
snow = tkinter.PhotoImage(file=r"img\snowflake.png")
sleet = tkinter.PhotoImage(file=r"img\sleet.png")
wind = tkinter.PhotoImage(file=r"img\wind.png")
fog = tkinter.PhotoImage(file=r"img\fog.png")
cloudy = tkinter.PhotoImage(file=r"img\cloud.png")
partly_cloudy = tkinter.PhotoImage(file=r"img\partly_cloudy.png")
partly_cloudy_night = tkinter.PhotoImage(file=r"img\night.png")
    
main_win.mainloop()