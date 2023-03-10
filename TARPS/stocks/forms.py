from django import forms

# stock prediction form
class TickerForm(forms.Form):

    ticker = forms.CharField(label='', max_length = 8)
    # timeLength = forms.ChoiceField(label="", choices = [('1m', '1m'), ('5m', '5m'), ('15m', '15m'), ('30m', '30m'), ('60m', '60m'), ('1d', '1d'),  ('5d', '5d'), ('1mo', '1mo')])
    timeLength = forms.ChoiceField(label="", choices = [('1m', '1 minute'), ('5m', '5 minutes'), ('15m', '15 minutes'), ('30m', '30 minutes'), ('60m', '60 minutes'), ('1d', '1 day'),  ('5d', '5 days'), ('1mo', '1 month')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
