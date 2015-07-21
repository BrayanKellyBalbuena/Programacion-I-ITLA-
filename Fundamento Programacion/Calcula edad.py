def eda():
    import datetime
    from datetime import date
    d=date.today()
    print(d.strftime('%d/%m/%y'))
    ano=int(input('Digite el ano >>>'))
    mes = int(input('Digite el mes >>>'))
    dia = int(input('Digite el dia >>>'))
    fecha_n = datetime.date(ano,mes,dia)
    cal = (d.year)-ano
    cal2=cal-1
    if mes < d.month:
        print("Su edad es",cal)
    elif mes == d.month and dia < d.day:
        print("Su edad es",cal-1)
    elif mes == d.month and dia >= d.day:
        print("Su edad es",cal)
    elif mes > d.month:
        print("Su edad es",cal-1)
    eda()
eda()       
