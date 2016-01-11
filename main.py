from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label

#TODO: rename this file to runnerslog.py
#TODO: put LogEntry and it's composition classes in another file

class TrainingType :
    def __init__(self, training_type) :
        self.__training_type = training_type
    @property
    def get_training_type(self) :
        return self.__training_type

class WeatherCondition :
    def __init__(self, weather_condition) :
        self.__weather_condition = weather_condition
    @property
    def get_weather_condition(self) :
        return self.__weather_condition

class LogEntry :
    #TODO: make these default values have sense
    def __init__(self, date = 0, weather_conditions = WeatherCondition('no weather condition given'), morning_pulse = 0, training_type = TrainingType('no training type given'), distance = 0, executed_time = 0, in_zone = 0, average_heart = 0) : 
        self.date = date
        # TODO: make a class of weather_conditions
        self.weather_conditions = WeatherCondition(weather_conditions)
        self.morning_pulse = morning_pulse
        # TODO: make a class of training_type
        self.training_type = TrainingType(training_type)
        self.distance = distance
        self.executed_time = executed_time
        self.in_zone = in_zone
        self.average_heart = average_heart

    @property
    def date(self) :
        return self.date_training
    @date.setter
    def date(self, date) :
        self.date_training = date

    @property
    def weather_conditions(self) :
        return self.weather_condition_training
    @weather_conditions.setter
    def weather_conditions(self, weather_condition) :
        self.weather_condition_training = weather_condition

    @property
    def morning_pulse(self) :
        return self.morning_pulse_training
    @morning_pulse.setter
    def morning_pulse(self, morning_pulse) :
        self.morning_pulse_training = morning_pulse

    @property
    def training_type(self) :
        return self.training_type_training
    @training_type.setter
    def training_type(self, training_type) :
        self.training_type_training = training_type

    @property
    def distance(self) :
        return self.distance_training
    @distance.setter
    def distance(self, distance) :
        self.distance_training = distance
    
    @property
    def executed_time(self) :
        return self.executed_time_training
    @executed_time.setter
    def executed_time(self, executed_time) :
       self.executed_time_training = executed_time
    
    @property
    def in_zone(self) :
        return self.in_zone_training
    @in_zone.setter
    def in_zone(self, in_zone) :
        self.in_zone_training = in_zone

    @property
    def average_heart(self) :
        return self.average_heart_training
    @average_heart.setter
    def average_heart(self, average_heart) :
        self.average_heart_training = average_heart

    def write_to_db(self) :
        # TODO: exception handling
        store = JsonStore('runners_log.json')
        # TODO: find a way to determine a unique key
        key = '1'
        # store.put(key, date = self.date, distance = self.distance, executed_time = self.executed_time, in_zone = self.in_zone, average_heart = self.average_heart, morning_pulse = self.morning_pulse, training_type = self.training_type.get_training_type(), weather_conditions = self.weather_conditions.get_weather_condition()) 
        store.put(key, date = self.date, distance = self.distance, executed_time =
                self.executed_time, in_zone = self.in_zone, average_heart =
                self.average_heart, morning_pulse = self.morning_pulse, training_type
                = 'self.training_type.get_training_type()', weather_conditions =
                'self.weather_conditions.get_weather_condition()') 

    def read_from_db(self) :
        # TODO: execption handling
        store = JsonStore('runners_log.json')
        key = '1'
        data = store.get(key)
        return data

class MyPageLayout(PageLayout) :
    pass

class AddTrainingLog(BoxLayout) :
    log_date = StringProperty()
    log_morning_pulse = StringProperty()
    log_training_type = StringProperty()
    log_distance = StringProperty()
    log_executed_time = StringProperty()
    log_in_zone = StringProperty()
    log_average_heart = StringProperty()
    log_weather_type = StringProperty()

    def on_submit(self) :
        print('on submit pressed')
        logentry = LogEntry(self.log_date, self.log_weather_type, self.log_morning_pulse,
                self.log_training_type, self.log_distance,
                self.log_executed_time, self.log_in_zone,
                self.log_average_heart)
        logentry.write_to_db()

class ConsultTrainingLog(BoxLayout) :
    average_heart = StringProperty()
    distance = StringProperty()
    in_zone = StringProperty()
    morning_pulse = StringProperty()
    weather_conditions = StringProperty()
    date = StringProperty()
    executed_time = StringProperty()
    training_type = StringProperty()

    def initialize(self) :
        logentry = LogEntry()
        data = logentry.read_from_db()
        print(data)
        self.average_heart = data['average_heart']
        self.distance = data['distance']
        self.in_zone = data['in_zone']
        self.morning_pulse = data['morning_pulse']
        self.weather_conditions = data['weather_conditions']
        self.date = data['date']
        self.executed_time = data['executed_time']
        self.training_type = data['training_type']

class RunnersLogApp(App) :
    def build(self) :
        myPageLayout = MyPageLayout()
        myPageLayout.add_widget(AddTrainingLog(), 1)
        consultTrainingLog = ConsultTrainingLog()
        consultTrainingLog.initialize()
        myPageLayout.add_widget(consultTrainingLog, 0)
        return myPageLayout

if __name__ == '__main__' :
    RunnersLogApp().run()
