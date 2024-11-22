# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# Sort the data in ascending order
file_names = [
    "report.docx",
    "presentation.pptx",
    "data.csv",
    "photo.jpg",
    "notes.txt",
    "invoice.pdf",
    "resume.docx",
    "budget.xlsx",
    "meeting.mp4",
    "schedule.pdf",
]

distances_traveled.sort()
print(distances_traveled)
daily_temperatures.sort(reverse=True)
print(daily_temperatures)
file_names.sort()
print(file_names)