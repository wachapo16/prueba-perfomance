# Prueba de Performance para Coordinadora

Este proyecto contiene pruebas de rendimiento para el servicio de recogidas de Coordinadora, específicamente para validar la capacidad del sistema de manejar el volumen de solicitudes proyectado.

## Descripción del Proyecto

El servicio de recogidas de Coordinadora está diseñado para manejar aproximadamente 9000 solicitudes diarias, con un pico de hasta el 70% de esas solicitudes entre las 7:30 am y 9:00 am. Además, se espera que la demanda del servicio crezca un 15% anualmente. Este proyecto de prueba de rendimiento verifica si la infraestructura actual puede soportar ese crecimiento durante los próximos cinco años.

## Pre-requisitos

Para ejecutar las pruebas de rendimiento, necesitarás instalar [Locust](https://locust.io/), una herramienta de prueba de carga distribuida escrita en Python.

## Instalación de Locust

Puedes instalar Locust usando pip:
```bash
pip install locust

## Comandos para ejecución de pruebas

Para correr las pruebas y generar reportes automáticamente, puedes usar el siguiente comando en tu terminal:
```bash
locust -f main.py


