"""
© https://sudipghimire.com.np
Create 3 different classes Length, Weight, and Time
Add respective attributes to store values.
Add static methods for conversion of different units.
Example:
    Length: cm to inches, kilometer to miles, etc
    Weight: KG to pounds, gram to Ounces, etc.
    Time: seconds to hours, milliseconds to seconds
    """

    # answer
#%%


class Length:
    @staticmethod
    def cm_to_inches(cm):
        return f'{cm} cm is {0.394*cm} inches.'
    @staticmethod
    def km_to_miles(km):
        return f'{km} km is {0.621*km} miles.'

print(Length.cm_to_inches(15))
print(Length.km_to_miles(100))

#%%


class Weight:
    @staticmethod
    def kg_to_lb(kg):
        return f'{kg} Kg is {2.204*kg} lb.'
    @staticmethod
    def gm_to_oz(gm):
        return f'{gm} gm is {0.035*gm} OZ.'


print(Weight.kg_to_lb(15))
print(Weight.gm_to_oz(100))

#%%


class Time:
    @staticmethod
    def sec_to_h(sec):
        return f'{sec} sec is {sec/3600} hour.'
    @staticmethod
    def milisec_to_sec(milisec):
        return f'{milisec} milisec is {0.001*milisec} second.'

print(Time.sec_to_h(3600))
print(Time.milisec_to_sec(1000000))

#%%