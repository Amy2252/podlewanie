from django.db import models
import tinytuya

# Create your models here.

class Power_Socket(models.Model):
    key=models.CharField(max_length=100)
    ip=models.CharField(max_length=100)
    local_key=models.CharField(max_length=100)
    def status(self):
        d=tinytuya.OutletDevice(self.key,self.ip,self.local_key)
        d.set_version(3.3)
        data=d.status()
        return data["dps"]["1"]
    def turn_on(self):
        d = tinytuya.OutletDevice(self.key, self.ip, self.local_key)
        d.set_version(3.3)
        d.turn_on()
    def turn_off(self):
        d = tinytuya.OutletDevice(self.key, self.ip, self.local_key)
        d.set_version(3.3)
        d.turn_off()

    


class Task(models.Model):
    socket=models.ForeignKey(Power_Socket,on_delete=models.CASCADE)
    duration=models.DurationField()
    start=models.DateTimeField()
    end=models.DateTimeField()
    complete=models.BooleanField()
