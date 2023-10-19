
'''
================================================
By Beni Honori
https://github.com/entediado97/Astrid_G-Maps
================================================
'''

# Importando as bibliotecas necessárias
import requests
from colorama import Fore, Style

# Função para verificar a vulnerabilidade da chave da API do Google Maps
def verificar_vulnerabilidade_gmaps(apikey):
    # Lista para armazenar APIs vulneráveis
    vulnerable_apis = []

    # Lista de URLs para verificar
    urls_to_check = [
        ("https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key=", "GET", "Custom Search", "$5 por 1000 requests", None),
        ("https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key=", "GET", "Custom Search", "$5 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key=", "GET", "Staticmap", "$2 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key=", "GET", "Streetview", "$7 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key=", "GET", "Directions", "$5 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=", "GET", "Geocode", "$5 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=", "GET", "Distance Matrix", "$5 por 1000 elements", None),
        ("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=", "GET", "Find Place From Text", "$17 por 1000 elements", None),
        ("https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key=", "GET", "Autocomplete", "$2.83 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key=", "GET", "Elevation", "$5 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key=", "GET", "Timezone", "$5 por 1000 requests", None),
        ("https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=", "GET", "Nearest Roads", "$10 por 1000 requests", None),
        ("https://www.googleapis.com/geolocation/v1/geolocate?key=", "POST", "Geolocation", "$5 por 1000 requests", {'considerIp': 'true'}),
        ("https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907&interpolate=true&key=", "GET", "Route to Traveled", "$10 por 1000 requests", None),
        ("https://roads.googleapis.com/v1/speedLimits?path=38.75807927603043,-9.03741754643809&key=", "GET", "Speed Limit-Roads", "$20 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key=", "GET", "Place Details", "$17 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=100&types=food&name=harbour&key=", "GET", "Nearby Search-Places", "$32 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key=", "GET", "Text Search-Places", "$32 por 1000 requests", None),
        ("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key=", "GET", "Places Photo", "$7 por 1000 requests", None),
        ("https://playablelocations.googleapis.com/v3:samplePlayableLocations?key=", "POST", "Playable Locations", "$10 por 1000 daily active users", {'area_filter':{'s2_cell_id':7715420662885515264},'criteria':[{'gameObjectType':1,'filter':{'maxLocationCount':4,'includedTypes':['food_and_drink']},'fields_to_return': {'paths': ['name']}},{'gameObjectType':2,'filter':{'maxLocationCount':4},'fields_to_return': {'paths': ['types', 'snapped_point']}}]}),
        ("https://fcm.googleapis.com/fcm/send", "POST", "FCM Takeover", "https://abss.me/posts/fcm-takeover/", {'registration_ids':['ABC']}),
        ("https://www.googleapis.com/customsearch/v1?cx=017576662512468239146:omuauf_lfve&q=lectures&key=", "GET", "Custom Search", "$5 por 1000 requisições", None),
        ("https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key=", "GET", "Staticmap", "$2 por 1000 requisições", None),        # Outros URLs aqui ...
    ]

    # Imprime cabeçalhos
    print('\n')
    #print("-" * 75)
    print(f"{Fore.BLUE}{'API':<30}{'Custo':<25}{'URL'}{Style.RESET_ALL}")
    print("-" * 75)

    # Loop para verificar cada URL
    for url, metodo, descricao, custo, dados_post in urls_to_check:
        url_completa = f"{url}{apikey}"
        
        try:
            # Se o método for GET, faça uma requisição GET
            if metodo == "GET":
                response = requests.get(url_completa)
            # Se o método for POST, faça uma requisição POST
            elif metodo == "POST":
                response = requests.post(url, json=dados_post)
            else:
                print(f"Tipo de método desconhecido: {metodo}")
                continue

            # Verifica se a resposta é 200 e se não contém erro
            if response.status_code == 200 and "error" not in response.text:
                print(f"{descricao:<30}{custo:<25}{Fore.GREEN}{url_completa}{Style.RESET_ALL}")
                vulnerable_apis.append((descricao, custo, url_completa))
            else:
                error_message = response.json().get("error", {}).get("message", "Erro desconhecido")
                print(f"{descricao:<30}{custo:<25}{Fore.RED}Não Vulnerável{Style.RESET_ALL}")
                print(f"Motivo: {Fore.YELLOW}{error_message}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{descricao:<30}{custo:<25}{Fore.RED}Erro: {e}{Style.RESET_ALL}")

    # Função para exportar os resultados
    exportar_relatorio(vulnerable_apis)

    # Imprime referências
    print("\nReferência para preços atualizados:")
    print("https://cloud.google.com/maps-platform/pricing")
    print("https://developers.google.com/maps/billing/gmp-billing")

# Função para exportar os resultados para um arquivo
def exportar_relatorio(vulnerable_apis):
    exportar = input(Fore.BLUE + "Deseja exportar um relatório para arquivo.txt? (Y/N): " + Style.RESET_ALL)
    if exportar.lower() == 'y':
        with open('POC.txt', 'w') as arquivo:
            arquivo.write("API || Custo || URL\n")
            for api in vulnerable_apis:
                arquivo.write(f"{api[0]} || {api[1]} || {api[2]}\n")
        print(Fore.BLUE + "Relatório exportado para arquivo.txt." + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "Relatório não exportado." + Style.RESET_ALL)

# Função principal
def main():
    print(Fore.BLUE + """
    #                                 ###            #####        #     #                          #####                       
   # #    ####  ##### #####  # #####  ###  ####     #     #       ##   ##   ##   #####   ####     #     #  ####    ##   #    # 
  #   #  #        #   #    # # #    #  #  #         #             # # # #  #  #  #    # #         #       #    #  #  #  ##   # 
 #     #  ####    #   #    # # #    # #    ####     #  #### ##### #  #  # #    # #    #  ####      #####  #      #    # # #  # 
 #######      #   #   #####  # #    #          #    #     #       #     # ###### #####       #          # #      ###### #  # # 
 #     # #    #   #   #   #  # #    #     #    #    #     #       #     # #    # #      #    #    #     # #    # #    # #   ## 
 #     #  ####    #   #    # # #####       ####      #####        #     # #    # #       ####      #####   ####  #    # #    # 
                                                                                                                               
                                                                                                                                                     
                                                                                                                                                     """ + Style.RESET_ALL)
    print("\nBem-vindo ao Astrid's G-Maps Scan!")
    print("Este programa verifica a vulnerabilidade da sua chave da API do Google Maps em várias APIs.")
    print("Certifique-se de ter uma chave de API válida antes de prosseguir.")
    
    apikey = input(Fore.BLUE +"\nPor favor, insira a chave da API do Google Maps que deseja testar: ")
    verificar_vulnerabilidade_gmaps(apikey)

if __name__ == "__main__":
    main()
