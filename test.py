import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define the internships with their details
internship_info = [
    {
        "company": "CeX Webuy",
        "start": "2021-07-01",
        "end": "2022-01-31",
        "description": "SQL, software dev, DASH app, Jira, GitHub, QA.",
        "color": "skyblue"
    },
    {
        "company": "Oriental FabriTech Pvt. Ltd.",
        "start": "2022-07-01",
        "end": "2023-11-30",
        "description": "Website design, security testing, enhanced sales.",
        "color": "orange"
    },
    {
        "company": "Techmentry",
        "start": "2023-06-01",
        "end": "2023-08-31",
        "description": "Robotics projects, drone development course, ROS, OpenCV.",
        "color": "green"
    },
    {
        "company": "1phi618",
        "start": "2023-09-01",
        "end": "2023-11-30",
        "description": "Python, Jupyter, NLP chatbots, SQL, AWS, HR automation.",
        "color": "red"
    },
    {
        "company": "DJS Antariksh",
        "start": "2021-10-01",
        "end": "2022-10-31",
        "description": "ROS, AI algorithms, rover navigation, documentation.",
        "color": "purple"
    },
    {
        "company": "DJS Antariksh (Head)",
        "start": "2022-10-01",
        "end": "2023-11-30",
        "description": "Training in ROS, MoveIt, autonomous navigation, Docker, GUI development.",
        "color": "brown"
    },
    {
        "company": "DJS Racing",
        "start": "2021-03-01",
        "end": "2023-02-28",
        "description": "ROS, vehicle harnessing, EV management, BMS, LiDAR.",
        "color": "pink"
    }
]

# Function to create the timeline
def create_timeline(internship_data, figure_path):
    # Setup the plot with a black background
    plt.figure(figsize=(14, 10), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')

    # # Define a range for the y-axis to accommodate the number of internships
    y_range = len(internship_data)
    ax.set_ylim(-1.5, y_range-7)  # Increase space at the bottom


    # Standardized bar height for uniform appearance
    standard_bar_height = 0.6

    # Create a white frame around the plot
    # for spine in ax.spines.values():
    #     spine.set_visible(True)
    #     spine.set_edgecolor('white')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set the y-axis with company names and white text
    ax.set_yticks(range(y_range))
    ax.set_yticklabels([internship["company"] for internship in internship_data], fontsize=12, color='white')

    # Format the x-axis to show dates with white text
    ax.xaxis_date()
    date_format = mdates.DateFormatter('%b %Y')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    # # Move the x-axis labels down to make space for the text
    # ax.tick_params(axis='x', which='major', pad=20)

    # # Add each internship as a bar in the timeline with the same height
    # for i, internship in enumerate(internship_data):
    #     start_date = mdates.date2num(datetime.strptime(internship["start"], '%Y-%m-%d'))
    #     end_date = mdates.date2num(datetime.strptime(internship["end"], '%Y-%m-%d'))
    #     ax.barh(i - 1.5, end_date - start_date, left=start_date, height=standard_bar_height, color=internship["color"], edgecolor='white')
    #     ax.text(start_date + (end_date - start_date) / 2, i - 1.5, internship['description'], ha='center', va='center', fontsize=9, color='white', weight='bold')

    # Set the title with white text
    plt.title('Internship Timeline', fontsize=16, color='white')

    # Save the figure
    plt.savefig(figure_path, facecolor='black')
    plt.close()  # Close the plot to prevent it from displaying now

# Call the function with your data and desired output path
create_timeline(internship_info, 'path_to_save_image7.png')
