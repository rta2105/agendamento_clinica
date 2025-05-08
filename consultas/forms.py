from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['psicologo', 'data', 'horario', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        psicologo = cleaned_data.get("psicologo")
        data = cleaned_data.get("data")
        horario = cleaned_data.get("horario")

        if psicologo and data and horario:
            conflito = Consulta.objects.filter(
                psicologo=psicologo,
                data=data,
                horario=horario
            ).exists()
            if conflito:
                raise forms.ValidationError(
                    "Esse horário já está agendado para o psicólogo selecionado."
                )
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['psicologo'].empty_label = "Selecione um psicólogo"
        self.fields['data'].widget.attrs.update({'class': 'form-control'})
        self.fields['horario'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['psicologo'].widget.attrs.update({'class': 'form-control'})
        self.fields['psicologo'].queryset = Consulta.objects.all()
        self.fields['psicologo'].label_from_instance = lambda obj: f"{obj.nome} ({obj.crp})"
        self.fields['psicologo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Selecione um psicólogo'})
        self.fields['observacoes'].label = "Observações (opcional)"
        self.fields['observacoes'].help_text = "Adicione qualquer observação relevante sobre a consulta."
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['observacoes'].required = False
        self.fields['observacoes'].label = "Observações (opcional)" 
    
    def clean_horario(self):
        horario = self.cleaned_data.get('horario')
        if horario and (horario.hour < 8 or horario.hour > 18):
            raise forms.ValidationError("O horário deve estar entre 08:00 e 18:00.")
        return horario
    
    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data and data < datetime.date.today():
            raise forms.ValidationError("A data não pode ser anterior a hoje.")
        return data
    
    def save(self, commit=True):
        consulta = super().save(commit=False)
        if commit:
            consulta.save()
        return consulta 
    
    
