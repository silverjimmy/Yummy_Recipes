"""Module for the Activity class"""
class Activity:
    """"Class creates activity objects """

    activity_id = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.activity_id = str(Activity.activity_id + 1)
        Activity.activity_id += 1
