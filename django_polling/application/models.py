from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract    = True
    
    date_created        = models.DateTimeField(auto_now_add=True)

class Poll(BaseModel):
    question            = models.CharField(max_length=500)
    
    @classmethod
    def get_current(cls):
        try:
            return cls.objects.all().order_by('-id')[0]
        except IndexError, e:
            return None
    
    def total_responses(self):
        return self.response_set.all().count()
    
class Answer(BaseModel):
    poll        = models.ForeignKey(Poll)
    answer_text = models.CharField(max_length=100)
    
    def get_total_responses(self):
        return self.response_set.all().count()

class Response(BaseModel):
    class InvalidAnswerIndexException(Exception): pass

    poll            = models.ForeignKey(Poll)
    mobile_number   = models.CharField(max_length=25, blank=True, null=True)
    answer          = models.ForeignKey(Answer)