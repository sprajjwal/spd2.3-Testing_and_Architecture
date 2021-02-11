# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """Instantiate a new OnBoardTemparatureSensor."""
        pass

    def read_voltage(self):    
        """Returns the voltage read."""    
        return 2.7

    def get_temperature(self):
        """Returns the Temperature read based on voltage."""
        return (
            self.read_voltage() * 
            OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
        )

 
class CarbonMonoxideSensor:

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """Instaniates a new CarbonMonoxideSensor object. 
        
        Args:
            temperature_sensor: an instance of OnBoardTemperatureSensor.
                                Use to initialize self.on_board_temp_sensor.
                                Sets up a new instance if missing.
                        
        Returns: None
        """
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Computes and returns the CO level based on the voltage."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = (
            CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
                sensor_voltage, self.on_board_temp_sensor.get_temperature()
            )
        )
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Reads and returns voltage from the sensor."""
        # In real life, it should read from hardware.        
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Converts voltage to CO level"""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:

    def __init__(self):
        """Initializes the class object."""
        self.string = ''

    def display(self, msg):
        """Displays message"""
        print(msg)


class CarbonMonoxideDevice():

    def __init__(self, co_sensor, display_unit):
        """Instantiate a CO device object.
        
        Args:
            co_sensor: a CarbonMonoxideSensor object
            display_unit: a DisplayUnit object

        Returns: None
        """
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit       

    def display(self):
        """Prints out the CO level on the display unit."""
        msg = (
            'Carbon Monoxide Level is : ' +
            str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        )
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()