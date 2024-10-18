#EMPLEADO DIRECTIVO
desempenoA="alto"
desempenoB="medio"
cargo1="directivo"
salarioDir1=3000000
salarioDir2=2500000
#EMPLEADO AUXILIAR
salarioAux=1300000
cargo2="auxiliar"
#EMPLEADO OPERATIVO
salarioOP=1750000
cargo3="operativo"
#BONIFICACIONES
bonificacionALT=20
bonificacionMED=10
#FUNCION SALARIO DIRECTIVO
def bonificacion_Directivo(cargo1,desempenoA,salarioDir1):
   if cargo1==1:
       cargo="directivo"
   elif bonificacionALT==2:
       cargo="directivo"
   elif desempenoA==2:
       salarioOP
   else:
       return salarioDir1
bonificacion_Directivo(cargo1,desempenoA,salarioDir1)

#FUNCION RESUMEN DE PAGO
boni = round(salarioDir1 * bonificacionALT)
total=(salarioDir1+boni)
def resumen_pago(cargo1,desempenoA,salarioDir1,bonificacionALT,bonificacionMED,total):
    if resumen_pago (f"Cargo: {cargo1}\n"
                    f"Nivel de Desempeño: {desempenoA}\n"
                    f"Salario Base: ${salarioDir1}\n"
                    f"Bonificacion: ${boni}\n"
                    f"Total a Recibir: ${total}")
resumen_pago(cargo1,desempenoA,salarioDir1,bonificacionALT,bonificacionMED,total)
