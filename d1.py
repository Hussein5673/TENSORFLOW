import os
from graphviz import Digraph

# Set the path to Graphviz executables (you need to adjust this to your system's path)
os.environ["PATH"] += ";C:\\Program Files\\Graphviz\\bin"

# Create a new directed graph for the Use Case Diagram
use_case = Digraph(comment='Fitness App Use Case Diagram')
use_case.attr(dpi='300', size='12,12', rankdir='LR')  # Improved layout

# Define Actors and their styling
use_case.node('User', 'User', shape='actor', style='filled', fillcolor='lightblue', fontsize=14)
use_case.node('Trainer', 'Trainer', shape='actor', style='filled', fillcolor='lightgreen', fontsize=14)
use_case.node('Admin', 'Admin', shape='actor', style='filled', fillcolor='lightyellow', fontsize=14)

# User use cases with styling
user_cases = ["Register / Login", "Update Profile", "Calculate BMI", "Get Trainer Suggestions", 
              "View Gyms Nearby", "Subscribe to Plan", "View Workout & Meal Plans", "Track Progress", 
              "Chat with Trainer", "Join Live Classes", "Participate in Challenges", "Use Chatbot"]
for case in user_cases:
    use_case.node(case, case, shape='ellipse', style='filled', fillcolor='lightcoral', fontsize=12, fontname='Helvetica')
    use_case.edge('User', case, color='blue')

# Trainer use cases with styling
trainer_cases = ["Manage Profile", "Create Workout Plan", "Create Meal Plan", "Track User Progress", 
                 "Host Live Classes", "Communicate with Users", "Participate in Challenges"]
for case in trainer_cases:
    use_case.node(case, case, shape='ellipse', style='filled', fillcolor='lightpink', fontsize=12, fontname='Helvetica')
    use_case.edge('Trainer', case, color='green')

# Admin use cases with styling
admin_cases = ["Manage Users", "View App Metrics", "Manage Subscriptions"]
for case in admin_cases:
    use_case.node(case, case, shape='ellipse', style='filled', fillcolor='lightgoldenrodyellow', fontsize=12, fontname='Helvetica')
    use_case.edge('Admin', case, color='orange')

# Optional: Add a title for clarity
use_case.attr(label='Fitness App Use Case Diagram', labelloc='t', fontsize=18, fontname='Helvetica-Bold')

# Render and save the file as PNG
use_case.render('fitness_app_use_case_diagram', format='png')
