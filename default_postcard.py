import matplotlib.pyplot as plt
import numpy as np


def main():
    fac = 2
    dimensions = np.array([148, 105])*fac

    mm = 1/25.4  # centimeters in inches
    fig = plt.figure(frameon=False, figsize=(dimensions[0]*mm, dimensions[1]*mm), dpi=100)
    # fig.set_size_inches(w, h)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    # ax.imshow(your_image, aspect='auto')
    # fig.savefig(fname, dpi)

    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    
    delta_base = 0.2
    delta_deci = 1.0
    
    linewidth = 0.5

    for ii in range(1, 100):
        delta = delta_base if ii%10 else delta_deci
        # Postive x
        ax.plot([ii, ii], [-delta, delta], 'k-', linewidth=linewidth,)
        
        # negativex 
        ax.plot([-ii, -ii], [-delta, delta], 'k-', linewidth=linewidth,)

        # Positive y
        ax.plot([-delta, delta], [ii, ii], 'k-', linewidth=linewidth,)
        
        # Negative y
        ax.plot([-delta, delta], [-ii, -ii], 'k-', linewidth=linewidth,)

        if not ii % 20:
            ax.text(ii-2, delta_deci + 1, f"{ii}%", fontsize='xx-small')
            ax.text(-(ii+2), delta_deci + 1, f"{ii}%", fontsize='xx-small')

            ax.text(delta_deci+1, ii-1, f"{ii}%", fontsize='xx-small')
            ax.text(delta_deci+1, -(ii+1), f"{ii}%", fontsize='xx-small')

    plt.show()

if (__name__) =="__main__":
    main()
