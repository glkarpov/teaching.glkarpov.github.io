import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch
import os

def create_pdf_cdf_animation(pdf_func, cdf_func, x_range, title, filename, 
                           save_dir='animations', color='g', alpha=0.4):
    """
    Generalized function to create PDF/CDF animation for any distribution
    
    Parameters:
    - pdf_func: function that takes x and returns PDF value
    - cdf_func: function that takes x and returns CDF value  
    - x_range: tuple (start, end, step) for x values
    - title: title for the plot
    - filename: name for saved animation (should end with .gif)
    - save_dir: directory to save animation (default: 'animations')
    - color: color for fill area and point (default: 'g')
    - alpha: transparency for fill area (default: 0.4)
    """
    # Create save directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
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
    ax_cdf.plot(x, y_cdf, color='darkred', label=r'$F_X(x)$', linewidth=2)
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
    
    # Add grid with 30% transparency
    ax_pdf.grid(True, alpha=0.5)
    ax_cdf.grid(True, alpha=0.5)
    
     # Initialize fill areas and points
    fill = ax_pdf.fill_between(x[:2], y_pdf[:2], color='r', alpha=0.5)
    path = fill.get_paths()[0]
    vertices = path.vertices
    point, = ax_cdf.plot(x[0], 0, "o", color='r', alpha=0.5, markersize=8)

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
        color=color, ls="dotted", linewidth=2
    )
    fig.add_artist(con)
    
    # Initialize text for CDF values
    cdf_text = ax_cdf.text(0.25, 0.85, '', transform=ax_cdf.transAxes, 
                          fontsize=12, bbox=dict(boxstyle='round', 
                          facecolor='lightyellow', alpha=0.8))
    
    def animate(i):
        if i == 0:
            # Initialize text for first frame
            current_x = x[i]
            current_y = y_cdf[i]
            cdf_text.set_text(f'x = {current_x:.1f}\nF({current_x:.1f}) = {current_y:.3f}')
            return point, fill, con, cdf_text
            
        # Update fill area
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
    filepath = os.path.join(save_dir, filename)
    writergif = animation.PillowWriter(fps=20)
    ani.save(filepath, writer=writergif)
    print(f"Animation saved as {filepath}")
    
    return ani

def create_two_point_animation(pdf_func, cdf_func, x_range, title, filename, 
                             save_dir='animations', delay_frames=20):
    """
    Create animation with two moving points showing CDF difference = probability
    
    Parameters:
    - pdf_func: function that takes x and returns PDF value
    - cdf_func: function that takes x and returns CDF value  
    - x_range: tuple (start, end, step) for x values
    - title: title for the plot
    - filename: name for saved animation (should end with .gif)
    - save_dir: directory to save animation (default: 'animations')
    - delay_frames: number of frames delay between leading and trailing point
    """
    # Create save directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    fig, (ax_pdf, ax_cdf) = plt.subplots(
        nrows=2,
        sharex=True,
        figsize=(10, 8),
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
    ax_cdf.plot(x, y_cdf, color='darkred', label=r'$F_X(x)$', linewidth=2)
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
    
    # Add grid with 30% transparency
    ax_pdf.grid(True, alpha=0.5)
    ax_cdf.grid(True, alpha=0.5)
    
    # Initialize fill areas and points
    # Leading point (green) - fills from start to current position
    fill_leading = ax_pdf.fill_between(x[:2], y_pdf[:2], color='g', alpha=0.5)
    path_leading = fill_leading.get_paths()[0]
    vertices_leading = path_leading.vertices
    
    # Trailing point (red) - fills from start to delayed position
    fill_trailing = ax_pdf.fill_between(x[:2], y_pdf[:2], color='r', alpha=0.5)
    path_trailing = fill_trailing.get_paths()[0]
    vertices_trailing = path_trailing.vertices
    
    # Two points on CDF plot
    point_leading, = ax_cdf.plot(x[0], 0, "o", color='g', alpha=0.7, markersize=8)
    point_trailing, = ax_cdf.plot(x[0], 0, "o", color='r', alpha=0.7, markersize=8)

    # Initialize connection lines
    con_leading = ConnectionPatch(
        (0, 0), (0, 0),
        "data", "data",
        axesA=ax_cdf, axesB=ax_pdf,
        color="g", ls="dotted", linewidth=2
    )
    con_trailing = ConnectionPatch(
        (0, 0), (0, 0),
        "data", "data",
        axesA=ax_cdf, axesB=ax_pdf,
        color="r", ls="dotted", linewidth=2
    )
    fig.add_artist(con_leading)
    fig.add_artist(con_trailing)
    
    # Initialize text for probability difference
    prob_text = ax_cdf.text(0.25, 0.85, '', transform=ax_cdf.transAxes, 
                           fontsize=12, bbox=dict(boxstyle='round', 
                           facecolor='lightyellow', alpha=0.8))
    
    def animate(i):
        if i == 0:
            # Initialize text for first frame
            current_x = x[i]
            current_y = y_cdf[i]
            prob_text.set_text(f'$x_a = x_b = {current_x:.1f}$\n$P(x_a < X < x_b) = F(x_b) - F(x_a) = 0.000$')
            return point_leading, point_trailing, fill_leading, fill_trailing, con_leading, con_trailing, prob_text
            
        # Calculate dynamic delay based on frame number
        total_frames = Nx
        leading_start_frame = int(0.4 * total_frames)  # Leading point goes to 60% of x-region
        
        if i < leading_start_frame:
            # Leading point moves alone, trailing point stays at start
            current_delay = i  # Trailing point is at frame 0
        else:
            # Leading point stops at leading_start_frame
            # Trailing point starts moving with same speed as leading point had
            # It takes leading_start_frame frames to catch up to the desired distance
            catch_up_frames = leading_start_frame
            trailing_start_frame = leading_start_frame
            
            if i < trailing_start_frame + catch_up_frames:
                # Trailing point is catching up with same speed as leading point had
                # delay decreases from leading_start_frame to delay_frames
                progress = (i - trailing_start_frame) / catch_up_frames
                current_delay = int(leading_start_frame * (1 - progress) + delay_frames * progress)
            else:
                # Both points move with constant delay
                current_delay = delay_frames
            
        # Leading point (green) - current position
        leading_idx = i
        trailing_idx = max(0, i - current_delay)
        
        # Update leading fill area (green)
        add_vert_leading = np.array([x[leading_idx], 0])
        path_leading = fill_leading.get_paths()[0]
        vertices_leading = path_leading.vertices
        vertices_leading[-1,0], vertices_leading[-1,1] = x[leading_idx], pdf_func(x[leading_idx])
        vertices_leading = np.vstack((vertices_leading, add_vert_leading))
        fill_leading.set_paths([vertices_leading], False)
        
        # Update trailing fill area (red)
        add_vert_trailing = np.array([x[trailing_idx], 0])
        path_trailing = fill_trailing.get_paths()[0]
        vertices_trailing = path_trailing.vertices
        vertices_trailing[-1,0], vertices_trailing[-1,1] = x[trailing_idx], pdf_func(x[trailing_idx])
        vertices_trailing = np.vstack((vertices_trailing, add_vert_trailing))
        fill_trailing.set_paths([vertices_trailing], False)
        
        # Update points and connections
        x_leading, y_leading = x[leading_idx], y_cdf[leading_idx]
        x_trailing, y_trailing = x[trailing_idx], y_cdf[trailing_idx]
        
        point_leading.set_data([x_leading], [y_leading])
        point_trailing.set_data([x_trailing], [y_trailing])
        
        con_leading.xy1 = x_leading, y_leading
        con_leading.xy2 = x_leading, 0
        con_trailing.xy1 = x_trailing, y_trailing
        con_trailing.xy2 = x_trailing, 0
        
        # Calculate probability difference
        prob_diff = y_leading - y_trailing
        
        # Update text with probability difference
        prob_text.set_text(f'$x_a = {x_trailing:.1f}$, $x_b = {x_leading:.1f}$\n$P(x_a < X < x_b) = F(x_b) - F(x_a) = {prob_diff:.3f}$')
        
        return point_leading, point_trailing, fill_leading, fill_trailing, con_leading, con_trailing, prob_text
    
    # Create animation
    fr = np.arange(Nx)
    ani = animation.FuncAnimation(
        fig,
        animate,
        interval=400,
        blit=False,
        frames=fr,
        repeat_delay=1000,
    )
    
    # Save animation
    filepath = os.path.join(save_dir, filename)
    writergif = animation.PillowWriter(fps=18)
    ani.save(filepath, writer=writergif)
    print(f"Two-point animation saved as {filepath}")
    
    return ani

# Example usage functions for different distributions

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

def exponential_pdf(x, rate=1):
    """PDF for exponential distribution with given rate"""
    if x < 0:
        return 0
    else:
        return rate * np.exp(-rate * x)

def exponential_cdf(x, rate=1):
    """CDF for exponential distribution with given rate"""
    if x < 0:
        return 0
    else:
        return 1 - np.exp(-rate * x)

def normal_pdf(x, mu=0, sigma=1):
    """PDF for normal distribution with mean mu and std sigma"""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def normal_cdf(x, mu=0, sigma=1):
    """CDF for normal distribution with mean mu and std sigma"""
    from scipy.stats import norm
    return norm.cdf(x, loc=mu, scale=sigma)

# Example usage
if __name__ == "__main__":
    # Create animations for different distributions
    
    # Uniform distribution (0 to 10)
    print("Creating uniform distribution animation...")
    create_pdf_cdf_animation(
        pdf_func=lambda x: uniform_pdf(x, 0, 10),
        cdf_func=lambda x: uniform_cdf(x, 0, 10),
        x_range=(-2, 12, 0.01),
        title="Uniform Distribution (0 to 10)",
        filename="uniform_0_10.gif"
    )
    
    # Exponential distribution
    print("Creating exponential distribution animation...")
    create_pdf_cdf_animation(
        pdf_func=lambda x: exponential_pdf(x, rate=0.5),
        cdf_func=lambda x: exponential_cdf(x, rate=0.5),
        x_range=(-1, 10, 0.01),
        title="Exponential Distribution (rate=0.5)",
        filename="exponential_0_5.gif",
        color='r'
    )
    
    # Two-point animation example
    print("Creating two-point animation...")
    create_two_point_animation(
        pdf_func=lambda x: uniform_pdf(x, 0, 10),
        cdf_func=lambda x: uniform_cdf(x, 0, 10),
        x_range=(-2, 12, 0.01),
        title="Two-Point Animation: CDF Difference = Probability",
        filename="two_point_uniform.gif",
        delay_frames=30
    )
    
    print("All animations created successfully!")
