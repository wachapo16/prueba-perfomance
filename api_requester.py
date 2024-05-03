from locust import HttpUser, task, between
from datetime import datetime
from address_generator import AddressGenerator
from date_generator import DateGenerator
from requests.exceptions import HTTPError

class APIRequester(HttpUser):
    wait_time = between(2, 5)
    daily_requests = 9000
    growth_rate = 0.15
    api_url = "https://apiv2-test.coordinadora.com/recogidas/cm-solicitud-recogidas-ms/solicitud-recogida"

    @task
    def make_request(self):
        try:
            future_date = DateGenerator.generate_future_date()
            random_address = AddressGenerator.generate_random_address()
        
            payload = {
                "tipoEnvio": "1",
                "tipoProducto": "4",
                "indicativo": "57",
                "tipoDocumento": "13",
                "email": "ana@gmail.com",
                "personaEntrega": "1",
                "indicativoEntrega": "57",
                "medidasAproximadas": [{"id": 2, "tipoPaq": "Par de zapatos", "nombrePaq": "Par de za...", "cantidad": 1}],
                "ciudad": "Envigado (Ant)",
                "via": "",
                "numero": "",
                "detalle": "PARQUE SAN JOSE BOD 14",
                "tipoVia": 16,
                "nombres": "prueba",
                "apellidos": "prueba1",
                "documento": "1036149000",
                "celular": "3005777777",
                "ciudadDetalle": {"nombre_terminal_operativa": "Medellin", "tipo_servicio": "A", "dane_ciudad": "05266",
                                  "dane_actual": "05266000", "ciudad_tarifa": "05266000", "sms": True,
                                  "cubre_mqp": True, "codigo_postal": "055428", "terminal_operativa": 2,
                                  "cubre_me": True, "area_telefono": 4, "observaciones2": "FCE - RD - FD - RCE",
                                  "codigo": "05266000", "tipo_poblacion": "D", "activo": True, "codigo_terminal": 2,
                                  "codigo_interno": 204, "mensajeria": True, "cubre_mm": False, "departamento": "05",
                                  "cubre_cm": False, "nombre": "Envigado (Ant)", "abreviado": "ENVIGADO",
                                  "nombre_terminal": "Medellin", "observaciones": ""},
                "direccion": random_address,
                "fechaRecogida": future_date,
                "nombreEntrega": "prueba",
                "apellidosEntrega": "prueba1",
                "celularEntrega": "3045677777",
                "emailUsuario": "anar.7@gmail.com",
                "descripcionTipoVia": "Kilómetro",
                "aplicativo": "envios"
            }
            self.client.post("/recogidas/cm-solicitud-recogidas-ms/solicitud-recogida", json=payload)
        except HTTPError as e:
            self.environment.runner.quit(f"HTTP error: {e}")

    def on_start(self):
        current_hour = datetime.now().hour
        current_year = datetime.now().year
        total_users = self.calculate_daily_requests(current_hour, current_year)

        for _ in range(total_users):
            self.make_request()

    def calculate_daily_requests(self, current_hour, current_year):
        peak_start_hour = 7
        peak_end_hour = 9

        daily_requests = self.daily_requests
        if peak_start_hour <= current_hour < peak_end_hour:
            daily_requests *= 0.7

        years_remaining = 5 - (current_year - datetime.now().year)
        daily_requests *= (1 + self.growth_rate) ** years_remaining

        return int(daily_requests)
