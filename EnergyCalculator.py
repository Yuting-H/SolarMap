import math


def SolarEnergyCalculator(df): 
    month_columns = df.iloc[:, 2:]
    monthly_sums = round(month_columns.sum(),2)

    # Convert the sums to a list
    monthly_sum_list = monthly_sums.tolist()

    ## Equation to Calculate Solar Energy A*Efficiency*irridance(amount of light)
    #Assumptions - Can have user edit it later
    area = 1.5  # m^2
    efficiency = 0.2  # 20%
    days = 30  # 1 month
    EnergySolar = []
    for s in monthly_sum_list:
        irridance = s/len(df) #In Kilowatt Hours
        P = irridance * area * efficiency
        E = round(P * days, 2)
        EnergySolar.append(E)
    
    return EnergySolar

def WindEnergyCalculator(df):
    
   ##  P = 1/2pAv^3n
    p = 1.225 #kg/m^3 air density
    r = 20 #m rotor radius
    A = 3.14 * r * r #A m^2 area of the rotor radius
    n = 0.4 # Efficiency
    t = 24 * 30 ## time - #of hours in a month
    month_columns = df.iloc[:, 2:]

    monthly_sums = round(month_columns.sum(),2)

    # Convert the sums to a list
    monthly_sum_list = monthly_sums.tolist()

    EnergyWind = []

    for s in monthly_sum_list:
        v = s/(len(df)) ## Wind speed
        P = p * A * math.pow(v,3) * (1/2) * 0.4
        E = round(P * t / math.pow(10,6), 2)
        EnergyWind.append(E)

    return EnergyWind




"""

To Plot - Saving the Code

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Annual"]

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(months, EnergyWind, color='b')

# Add titles and labels
plt.title('Monthly Wind Energy Output (MWh)')
plt.xlabel('Month')
plt.ylabel('Energy Output (MWh)')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, EnergySolar, color='b')

# Add titles and labels
plt.title('Monthly Solar Energy Output (KWh)')
plt.xlabel('Month')
plt.ylabel('Energy Output (KWh)')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
"""