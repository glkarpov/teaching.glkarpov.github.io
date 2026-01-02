import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch
import os

# Create animations directory if it doesn't exist
if not os.path.exists('animations'):
    os.makedirs('animations')

def pdf(x):
    if (x < 1):
        return 0
    elif (x >= 1) and (x <= 5):
        return (5 / 4) * (1 / (x ** 2))
    else:
        return 0

def cdf(x):
    if (x < 1):
        return 0
    elif (x >= 1) and (x <= 5):
        return (5*x - 5) / (4 * x)
    else:
        return 1

def uniform_pdf(x, a=0, b=10):
    """PDF for uniform distribution on [a, b]"""
    if x < a or x > b:
        return 0
    else:
        return 1 / (b - a)

def uniform_cdf(x, a=0, b=10):
    """CDF for uniform distribution on [a, b]"""
    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return (x - a) / (b - a)

def create_animation(pdf_func, cdf_func, x_range, title, filename, a=0, b=10):
    """
    Generalized function to create PDF/CDF animation
    
    Parameters:
    - pdf_func: function that takes x and returns PDF value
    - cdf_func: function that takes x and returns CDF value  
    - x_range: tuple (start, end, step) for x values
    - title: title for the plot
    - filename: name for saved animation
    - a, b: parameters for distribution (used in uniform case)
    """
    fig, (ax_pdf, ax_cdf) = plt.subplots(
        nrows=2,
        sharex=True,
        figsize=(8, 8),
    )
    
    plt.rcParams['axes.grid'] = True
    plt.rc('legend', fontsize=12)
    fig.suptitle(title, fontsize=16)
    
    x = np.arange(x_range[0], x_range[1], x_range[2])
    Nx = x.shape[0]
    y_pdf = np.empty((Nx))
    y_cdf = np.empty((Nx))
    
    for i in range(Nx):
        y_pdf[i] = pdf_func(x[i])
    for i in range(Nx):
        y_cdf[i] = cdf_func(x[i])
    
    # Plot the curves
    ax_cdf.plot(x, y_cdf, label=r'$F_X(x)$', linewidth=2)
    ax_pdf.plot(x, y_pdf, label=r'$f_X(x)$', linewidth=2)
    
    ax_pdf.legend()
    ax_cdf.legend()
    
    # Set labels
    ax_pdf.set_ylabel('PDF')
    ax_cdf.set_ylabel('CDF')
    ax_cdf.set_xlabel('x')
    
    # Set y-axis limits
    ax_pdf.set_ylim(0, max(y_pdf) * 1.1)
    ax_cdf.set_ylim(0, 1.1)
    
    # Show y-axis on both plots
    ax_pdf.spines['left'].set_visible(True)
    ax_cdf.spines['left'].set_visible(True)
    ax_pdf.tick_params(left=True, labelleft=True)
    ax_cdf.tick_params(left=True, labelleft=True)
    ax_pdf.grid(True, alpha=0.3)
    ax_cdf.grid(True, alpha=0.3)
    
    # Initialize fill areas and points
    fill = ax_pdf.fill_between(x[:2], y_pdf[:2], color='r', alpha=0.5)
    path = fill.get_paths()[0]
    vertices = path.vertices
    point, = ax_cdf.plot(x[0], 0, "o", color='r')

    global tmp_vert
    tmp_vert = np.zeros((2,2))
    tmp_vert[0, 0], tmp_vert[0,0] = x[0], 0
    tmp_vert[1, 0], tmp_vert[1,1] = x[0], 0
    fill.set_paths([tmp_vert], False)
    
    # Initialize connection line
    con = ConnectionPatch(
        (0, 0), (0, 0),
        "data", "data",
        axesA=ax_cdf, axesB=ax_pdf,
        color="g", ls="dotted", linewidth=2
    )
    fig.add_artist(con)
    
    # Initialize text for CDF values
    cdf_text = ax_cdf.text(0.02, 0., '', transform=ax_cdf.transAxes, 
                          fontsize=12, bbox=dict(boxstyle='round', 
                          facecolor='lightyellow', alpha=0.8))
    
    def animate(i):
        if i == 0:
            # Initialize text for first frame
            current_x = x[i]
            current_y = y_cdf[i]
            cdf_text.set_text(f'x = {current_x:.1f}\nF({current_x:.1f}) = {current_y:.3f}')
            return point, fill, con, cdf_text
            
        add_vert = np.array([x[i], 0])
        path = fill.get_paths()[0]
        vertices = path.vertices
        vertices[-1,0], vertices[-1,1] = x[i], pdf_func(x[i])
        vertices = np.vstack((vertices, add_vert))
        fill.set_paths([vertices], False)
        
        # Update point and connection
        x_point, y_point = x[i], y_cdf[i]
        point.set_data([x_point], [y_point])
        con.xy1 = x_point, y_point
        con.xy2 = x_point, 0
        
        # Update text with current CDF value
        cdf_text.set_text(f'x = {x_point:.1f}\nF({x_point:.1f}) = {y_point:.3f}')
        
        return point, fill, con, cdf_text
    
    # Create animation
    fr = np.arange(Nx)
    ani = animation.FuncAnimation(
        fig,
        animate,
        interval=50,
        blit=False,
        frames=fr,
        repeat_delay=1000,
    )
    
    # Save animation
    filepath = os.path.join('animations', filename)
    writergif = animation.PillowWriter(fps=20)
    ani.save(filepath, writer=writergif)
    print(f"Animation saved as {filepath}")
    
    return ani

# Example 1: Original distribution (1 to 5)
print("Creating animation for original distribution...")
ani1 = create_animation(
    pdf_func=pdf,
    cdf_func=cdf,
    x_range=(-1, 8, 0.01),
    title="Original Distribution (1 to 5)",
    filename="original_distribution.gif"
)

# Example 2: Uniform distribution (0 to 10)
print("Creating animation for uniform distribution...")
ani2 = create_animation(
    pdf_func=lambda x: uniform_pdf(x, 0, 10),
    cdf_func=lambda x: uniform_cdf(x, 0, 10),
    x_range=(-2, 12, 0.01),
    title="Uniform Distribution (0 to 10)",
    filename="uniform_distribution.gif"
)

# Example 3: Uniform distribution (0 to 5) for comparison
print("Creating animation for uniform distribution (0 to 5)...")
ani3 = create_animation(
    pdf_func=lambda x: uniform_pdf(x, 0, 5),
    cdf_func=lambda x: uniform_cdf(x, 0, 5),
    x_range=(-1, 7, 0.01),
    title="Uniform Distribution (0 to 5)",
    filename="uniform_distribution_0_5.gif"
)

print("All animations created successfully!")
