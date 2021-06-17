##Third party imports
##Third party imports
from articles.models import Article
from django.db import models
from django.core.mail import EmailMessage
##Local application imports
from users.models import User
from billing import TMPDIR, PURCHASES_EMAIL
##Module imports
import csv
import os
import arrow
from smtplib import SMTP, SMTPException

class Bill(models.Model):
    bill_id = models.CharField(max_length=25, editable=False)
    bill_date = models.DateField(auto_now_add=True, editable=False)
    client = models.ForeignKey(User, blank=False, null=False, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        today = arrow.now()
        ##Asignamos un código que incluya información de la fecha para incrementar legibilidad
        self.bill_id = f"{today.day}_{today.year}_{str(today.timestamp())[:8]}"
        self.create_csv()
        
        super(Bill, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.bill_id
    
    def create_csv(self):
        
        amount = 0
        purchases = BillingBody.objects.filter(bill=self.pk)
        
        if not os.path.isdir(TMPDIR):
            os.mkdir(TMPDIR)
        filename = f"Factura {arrow.now().year}_{arrow.now().month}_{arrow.now().day}.csv"
        with open(f"{TMPDIR}/{filename}", 'w') as f:
        # with open('employee_file.csv', mode='w') as employee_file:
            employee_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(["ID FACTURA", self.bill_id, self.User.first_name, self.User.last_name, self.bill_date])
            for purchase in purchases:
                employee_writer.writerow([purchase.article.code, purchase.article.name, purchase.article.price])
                amount += purchase.article.price 
            employee_writer.writerow(["Total", amount])
            
            email = EmailMessage(
                subject=f"Su compra en Zapatos Bernini {self.bill_id}",
                from_email=self.User.email,
                to=[PURCHASES_EMAIL, ]
            )
            email.attach_file(f"{os.getcwd()}/{TMPDIR}/{filename}")
            
            try:
                email.send()
            except SMTPException:
                print(f"No se pudo enviar el correo a {PURCHASES_EMAIL}")
    
class BillingBody(models.Model):
    bill = models.ForeignKey(Bill, blank=False, null=False, verbose_name='Factura', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='Artículo', on_delete=models.CASCADE)
