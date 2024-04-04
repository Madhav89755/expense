# Generated by Django 5.0.4 on 2024-04-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0003_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('loan-repayment', 'Loan-Repayment'), ('loan-given', 'Loan-Given'), ('uncategorized', 'Uncategorized'), ('food', 'Food'), ('travel', 'Travel'), ('salary', 'Salary'), ('income', 'Income'), ('fd', 'FD'), ('rd', 'RD'), ('invoice-payment', 'Inovice-Payment')], default='food', max_length=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('added', 'Credit'), ('debit', 'Debit')], default='debit', max_length=20),
        ),
    ]