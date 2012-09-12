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
    poll                = models.ForeignKey(Poll)
    answer              = models.CharField(max_length=100)

class Response(BaseModel):
    class InvalidAnswerIndexException(Exception): pass

    poll                = models.ForeignKey(Poll)
    answer_index        = models.PositiveIntegerField()
    
    def save(self, *args, **kwargs):
        if self.answer_index <= 0 or self.answer_index > self.poll.answer_set.all().count():
            raise InvalidAnswerIndexException("Answer index does not fall in line with the answers available!")
        
        super(Response, self).save(*args, **kwargs)
