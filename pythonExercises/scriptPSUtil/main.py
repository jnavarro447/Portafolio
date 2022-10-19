import psutil



def get_total_disk_capacity_gb():
    totalUsage = psutil.disk_usage("/").total / (1024.0**3)
    totalInGB = totalUsage.__ceil__()
    return totalInGB


def get_percent_diskusage():
    return psutil.disk_usage("/").percent


def get_cpu_usage_percent():
    return psutil.cpu_percent(1)


def get_cpu_usage_user(obj):
    return obj.user


def get_cpu_usage_nice(obj):
    return obj.nice


def get_cpu_usage_system(obj):
    return obj.system


def get_cpu_usage_idle(obj):
    return obj.idle


def get_battery_object():
    return psutil.sensors_battery()


def get_battery_percent():
    objBattery = get_battery_object()
    return objBattery.percent


def is_battery_plugged():
    objBattery = get_battery_object()
    return objBattery.power_plugged


print("Espacio total: " + str(get_total_disk_capacity_gb()) + " GB")

# Obtiene el uso del disco en porcentaje
disk_Capacity_Percent = get_percent_diskusage()
print(str(disk_Capacity_Percent) + "% del disco esta en uso.")

# Condicional si el porcentaje de uso es mayor a 80 imprime mensaje a usuario
if disk_Capacity_Percent >= 80:
    print("\n**********************************************")
    print("** Capacidad del disco se encuentra al 80%  **")
    print("**********************************************\n")


print("Uso del CPU: " + str(get_cpu_usage_percent()) + "%")
# Obtener los valores del uso del CPU de los segmentos
cpuTimes = psutil.cpu_times_percent()

print("\tUser " + str(get_cpu_usage_user(cpuTimes)) + "%; ",
      "Nice " + str(get_cpu_usage_nice(cpuTimes)) + "%; ",
      "System " + str(get_cpu_usage_system(cpuTimes)) + "%; ",
      "Idle " + str(get_cpu_usage_idle(cpuTimes)) + "%")


print("Bateria al " + str(get_battery_percent()) + "%")


if not is_battery_plugged():
    print("\n**************************")
    print("**  Conectar bateria    **")
    print("**************************")
