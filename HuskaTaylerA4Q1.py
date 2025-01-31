"""HuskaTaylerA4Q1
AUTHOR [TAYLER HUSKA]
VERSION [2024-DEC-9]
PURPOSE [CREATE STAR AND CONSTELATION MAPPING PROGRAM]
"""
import numpy as np
import matplotlib.pyplot as plt

# Step 1
def get_stars_info():
    '''get_stars_info opens the user given file and parses though the information to return
    a dict with the hd as the key and the x,y  coordinated, magnitute, hr number and alternitive 
    names and the value, and star_name_dict with the name as the key and its x and y coordinates 

    as the value
    Input:
    nothing
    Output:
    tuple of stars_info, star_name_dict'''

    stars_info = {}
    star_name_dict = {} #to help out with the constelation later
    file = input("Which star file would you like to open?: ")
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            values = line.split(',')
            x_cor = float(values[0])
            y_cor = float(values[1])
            hd = float(values[3])
            mag = float(values[4])
            #print(mag)
            hr = float(values[5])
            # may be some lines without alt names, so a seperate case must be made
            if len(values) > 6:
                names = values[6:]
                stars_info[hd] = x_cor, y_cor, mag, hr, names
                for name in names:
                        string_name = ''.join(name)
                        string_name = string_name.split(';')
                        for ea_name in string_name:
                            star_name_dict[ea_name] = x_cor, y_cor
            else:
                stars_info[hd] = x_cor, y_cor, mag, hr

    return stars_info, star_name_dict

# Step 2
def get_limiting_mag(stars_info):
    '''get_limiting_mag takes the previously made stars_info dictionary and filters
    the information according to the magnitude greater than or equal to the user entered limiting

    magnitude, then returns x_y_mag_arr and lim_mag_sub
    Input:
    stars_info dictionary of all the stars information
    Output:
    tuple of x_y_arr which contains the same strucuture of stars_info, except only containing the allowed
    magnitudes and lim_mag_sub which is the limiting magnitude plus one which all the magnitudes will be
    subtracted by for plotting their size later on'''

    lim_mag = float(input("Please enter the limiting magnitude: "))
    mag_arr = []
    x_cor_arr = []
    y_cor_arr = []
    for key, value in stars_info.items():
        # if there is an alt name given
        if len(value) > 4:
            # if there is alt names given
            x_cor, y_cor, mag, hr, names = stars_info[key]
            if mag <= lim_mag:
                mag_arr.append(mag)
                x_cor_arr.append(x_cor)
                y_cor_arr.append(y_cor)
        # if no alt name is given
        else: 
            x_cor, y_cor, mag, hr = stars_info[key]
            if mag <= lim_mag:
                mag_arr.append(mag)
                x_cor_arr.append(x_cor)
                y_cor_arr.append(y_cor)

    x_y_mag_arr = np.array([x_cor_arr, y_cor_arr, mag_arr])
    lim_mag_sub = lim_mag + 1

    return x_y_mag_arr, lim_mag_sub
          
# Step 3
def plot_stars(x_y_mag_arr, lim_mag_sub):
    '''plot_stars job is to accept a_y_mag_arr and lim_mag_sub and use matplotlib to graph the
    stars accorining to their magnitude and postion given. lim_mag_sub is used to control the size

    Input:
    x_y_mag, lim_mag_sub
    Output:
    scatter plot of the stars in matplotlib (not to be shown yet)'''

    x_star = x_y_mag_arr[0].tolist()
    y_star = x_y_mag_arr[1].tolist()
    mags = x_y_mag_arr[2]
    #print(mags)
    size = lim_mag_sub - mags
    size = size ** 3
    plt.scatter(
        x_star, 
        y_star, 
        s = size, 
        c='k'
    )

# Step 4
def plot_constelation(star_name_dict): 
    '''Plot constelation acccepts the stars_name_dict made in the get_stars_info funtion to allow
    for easier fiding of the coordinates and goes though each line in the user input file of stars
    of the given constelation to graph onto the previously graphed star graph
    
    Input:
    stars_name_dict
    Output:
    shows the graph of the stars and the graphed constelation'''

    constel_file = input("Please enter your constelation file: ")
    star_chart = {}
    with open(constel_file) as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip().split(",")
            star_1 = line[0]
            star_2 = line[1]
            x1,y1 = star_name_dict[star_1]
            x2,y2 = star_name_dict[star_2]
# not quite sure what was wanted with the star chart but I added it to be safe
            #star_chart[star_1] = x1, y1
            #star_chart[star_2] = x2,y2

            plt.plot([x1,x2],[y1,y2], lw = 1, c = 'g')

    plt.show()

def main():
    running = True
    while running:
        stars_info, star_name_dict = get_stars_info()
        x_y_mag_arr, lim_mag_sub = get_limiting_mag(stars_info)
        plot_stars(x_y_mag_arr, lim_mag_sub)
        plot_constelation(star_name_dict)
        print("Graphing finished, program terminated.")
        running = False


if __name__ == '__main__':
    main()