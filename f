import os
from graphviz import Digraph

# Set the path to Graphviz executables
os.environ["PATH"] += r";C:\Program Files\Graphviz\bin"

# Create a new directed graph for the Use Case Diagram
use_case = Digraph(comment='Fitness App Use Case Diagram')
use_case.attr(dpi='300', size='10,10', fontname='Helvetica')

# Add a rectangular boundary around use cases
with use_case.subgraph(name='cluster_0') as frame:
    frame.attr(style='filled', color='lightyellow', label='Fitness App Use Case Diagram', labelloc='t', fontsize='16', fontname='Helvetica-Bold')

    # Define Admin actor and use cases on the left side
    with frame.subgraph(name='cluster_admin') as admin_group:
        admin_group.attr(label='', color='none')  # No border around each actor group for simplicity
        admin_group.node('Admin', '👤 Admin', shape='plaintext', fontsize='14', fontcolor='orange')
        
        # Admin use cases
        admin_cases = ["Manage Users", "View App Metrics", "Manage Subscriptions"]
        for case in admin_cases:
            admin_group.node(case, case, shape='ellipse', style='filled', fillcolor='lightblue', fontcolor='black', fontsize='10', fontname='Helvetica')
            admin_group.edge('Admin', case, color='black')

    # Define Trainer actor and use cases next to Admin
    with frame.subgraph(name='cluster_trainer') as trainer_group:
        trainer_group.attr(label='', color='none')
        trainer_group.node('Trainer', '👤 Trainer', shape='plaintext', fontsize='14', fontcolor='purple')
        
        # Trainer use cases
        trainer_cases = ["Manage Profile", "Create Workout Plan", "Create Meal Plan", "Track User Progress", 
                         "Host Live Classes", "Communicate with Users", "Participate in Challenges"]
        for case in trainer_cases:
            trainer_group.node(case, case, shape='ellipse', style='filled', fillcolor='lightblue', fontcolor='black', fontsize='10', fontname='Helvetica')
            trainer_group.edge('Trainer', case, color='black')

    # Define User actor and use cases on the right side
    with frame.subgraph(name='cluster_user') as user_group:
        user_group.attr(label='', color='none')
        user_group.node('User', '👤 User', shape='plaintext', fontsize='14', fontcolor='red')
        
        # User use cases
        user_cases = ["Register / Login", "Update Profile", "Calculate BMI", "Get Trainer Suggestions", 
                      "View Gyms Nearby", "Subscribe to Plan", "View Workout & Meal Plans", "Track Progress", 
                      "Chat with Trainer", "Join Live Classes", "Participate in Challenges", "Use Chatbot"]

        for case in user_cases:
            user_group.node(case, case, shape='ellipse', style='filled', fillcolor='lightblue', fontcolor='black', fontsize='10', fontname='Helvetica')
            user_group.edge('User', case, color='black')

# Render and save the file as PNG
use_case.render('5fitness_app_use_case_diagram_clear', format='png', cleanup=True)
