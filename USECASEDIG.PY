import matplotlib.pyplot as plt  # <-- THIS WAS MISSING
import matplotlib.patches as patches

def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Actor
    ax.add_patch(patches.Circle((1, 4), 0.5, fc='lightgray'))
    ax.text(1, 3.2, "User", ha='center')
    
    # Use Cases
    cases = [
        ("Select\nLength", 4, 6),
        ("Select\nChar Types", 7, 6),
        ("Generate\nPassword", 4, 4),
        ("View\nPassword", 7, 4),
        ("Copy\nPassword", 5.5, 2)
    ]
    
    for text, x, y in cases:
        ax.add_patch(patches.Ellipse((x, y), 2.5, 1.2, fc='yellow', ec='black'))
        ax.text(x, y, text, ha='center', va='center')
    
    # Connections
    for case in cases:
        ax.plot([1.5, case[1]-1], [4, case[2]], 'k-', lw=1)
    
    plt.savefig('use_case.png', bbox_inches='tight')
    plt.close()  # <-- Prevents memory leaks
    print("Use case diagram saved as use_case.png")

create_use_case_diagram()
