import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        #TODO: Calculate the mean of the data set. Remember that the data set is stored in self.data
        # Change the value of the mean attribute to be the mean of the data set
        # Return the mean of the data set   
        self.mean=sum(self.data)/len(self.data)
        return self.mean
        #pass
                
    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """
        # TODO:
        #   Calculate the standard deviation of the data set
        #   
        #   The sample variable determines if the data set contains a sample or a population
        #   If sample = True, this means the data is a sample. 
        #   Keep the value of sample in mind for calculating the standard deviation
        #
        #   Make sure to update self.stdev and return the standard deviation as well    
        sigma=0
        mn=self.mean
        if sample:
            n=len(self.data)-1
        else:
            n=len(self.data)

        for i in self.data:
            sigma += (i-mn)**2
        
        sigma = math.sqrt(sigma / n)
        self.stdev = sigma
        
        return self.stdev

    def read_data_file(self, file_name, sample=True):
    
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name, 'r') as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        # TODO: 
        #   Update the self.data attribute with the data_list
        #   Update self.mean with the mean of the data_list. 
        #       You can use the calculate_mean() method with self.calculate_mean()
        #   Update self.stdev with the standard deviation of the data_list. Use the 
        #       calcaulte_stdev() method.
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        # DONE: Plot a histogram of the data_list using the matplotlib package.
        #       Be sure to label the x and y axes and also give the chart a title
        plt.hist(self.data)
        plt.title('Histogram for Udacity project')
        plt.xlabel('Data')
        plt.ylabel('frequency')

        plt.show()

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        # TODO: Calculate the probability density function of the Gaussian distribution
        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation
        return (1.0/math.sqrt(2*math.pi*self.stdev**2))*math.exp(-((x-self.mean)**2)/2*self.stdev**2)
        #pass     

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        #TODO: Nothing to do for this method. Try it out and see how it works.
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
guassian_one=Gaussian()
guassian_one.read_data_file('C:/Users/Davie/Data/UdacityAPI/numbers.txt')
print(guassian_one.mean)
print(guassian_one.stdev)

guassian_one.plot_histogram()

guassian_one.plot_histogram_pdf();


# INHERITANCE
class Distribution:
    def __init__(self, mu=0, sigma=1):
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file

            """

        self.mean = mu
        self.stdev = sigma
        self.data = []


#read_data_file function

    def read_data_file(self, file_name):
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list

#Gaussian class

import math

import matplotlib.pyplot as plt

class Gaussian(Distribution):

    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0, sigma=1): 
        Distribution.__init__(self, mu, sigma) 

    def calculate_mean(self):    
        """Function to calculate the mean of the data set. 
        Args: 
            None
        Returns: 
            float: mean of the data set
        """

        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg        
        return self.mean

    def calculate_stdev(self, sample=True):
        """Function to calculate the standard deviation of the data set.
        Args: 
            sample (bool): whether the data represents a sample or population
        Returns: 
            float: standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.calculate_mean()   
        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2        

        sigma = math.sqrt(sigma / n) 
        self.stdev = sigma

        return self.stdev  

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        Args:
            None
        Returns:
            None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')     

    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.        
        Args:
            x (float): point for calculating the probability density function           
        Returns:
            float: probability density function output
        """        

        return (1.0 / (self.stdev  *math.sqrt(2*math.pi)))  *math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)        


    def plot_histogram_pdf(self, n_spaces = 50):
        """Function to plot the normalized histogram of the data and a plot of the probability density function along the same range        

        Args:
            n_spaces (int): number of data points
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """

        mu = self.mean
        sigma = self.stdev
        min_range = min(self.data)
        max_range = max(self.data)

         # calculates the interval between x values

        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize

        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')

        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):    
        """Function to add together two Gaussian distributions
        Args:
            other (Gaussian): Gaussian instance
        Returns:
            Gaussian: Gaussian distribution
            """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev  **2 + other.stdev**  2)

        return result

    def __repr__(self):
                        
            """Function to output the characteristics of the Gaussian instance
       Args:
            None
       Returns:
                string: characteristics of the Gaussian
        """
            return "mean {}, standard deviation {}".format(self.mean, self.stdev)