from django.db import models

class Goal(models.Model):
    description = models.CharField(max_length=200, default='')
    current_amount = models.IntegerField(default=0)
    goal_amount = models.IntegerField()
    end_date = models.DateTimeField('Due')

    def __str__(self):
        return str(self.current_amount) + ' / ' + str(self.goal_amount) + ' : ' + str(self.end_date)
