from django.db import models

class Goal(models.Model):
    description = models.CharField(max_length=200, default='')
    current_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    goal_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    end_date = models.DateField('Due')

    def __str__(self):
        return str(self.current_amount) + ' / ' + str(self.goal_amount) + ' : ' + str(self.end_date)

class Transaction(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.amount
