import json as j, shutil, tempfile
from collections import OrderedDict


def UpdateDataWriteJSON(data):
    # variavel que salva o id do paciente
    dataSave = data.decode('utf-8').split(",")
    
    #inicia a escrito no documento JSON
    with open('pacientes.json', 'r+', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        
        #print(j.load(arq))
        # ler todo o arquivo e obter o objeto JSON
        jsonLoad = j.load(arq)
        arq.close()
        
        
        # atualizar os dados com um novo paciente
        if dataSave[0] not in jsonLoad:
            
            y = {dataSave[0]: {
                    dataSave[1] : dataSave[2],
                    dataSave[3] : dataSave[4],
                    dataSave[5] : dataSave[6],
                    dataSave[7] : dataSave[8],
                    dataSave[9] : dataSave[10],
                    dataSave[11] : dataSave[12],
                    dataSave[13] : dataSave[14],
                    dataSave[15] : dataSave[16],
                    dataSave[17] : dataSave[18]
                    }
                }
    
            jsonLoad.update(y) 
            
            j.dump(jsonLoad, out, ensure_ascii=False, indent=4, separators=(',',':'))
            
        else:
            # atualizar os dados do paciente conectado
            jsonLoad[dataSave[0]][dataSave[1]] = dataSave[2]
            jsonLoad[dataSave[0]][dataSave[3]] = dataSave[4]
            jsonLoad[dataSave[0]][dataSave[5]] = dataSave[6]
            jsonLoad[dataSave[0]][dataSave[7]] = dataSave[8]
            jsonLoad[dataSave[0]][dataSave[9]] = dataSave[10]
            jsonLoad[dataSave[0]][dataSave[11]] = dataSave[12]
            jsonLoad[dataSave[0]][dataSave[13]] = dataSave[14]
            
            
            #Temperatura
            if int(dataSave[6]) >= 38:   
                x = int(dataSave[18])
                x = x + 1
                jsonLoad[dataSave[0]][dataSave[17]] = x                
            else:
                x = int(dataSave[18])
                x = x + 0
                jsonLoad[dataSave[0]][dataSave[17]] = x
            
            
            # Pontuacao Pressao Arterial
            if int(dataSave[8]) < 72:
                x = x + 3
                jsonLoad[dataSave[0]][dataSave[17]] = x
            elif int(dataSave[8]) < 81: 
                x = x + 2
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            elif int(dataSave[8]) < 100:
                x = x + 1
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            else:
                x = x + 0
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            # Frequencia Respiratoria
            if int(dataSave[10]) > 25:
                x = x + 3
                jsonLoad[dataSave[0]][dataSave[17]] = x
            elif int(dataSave[10]) > 20: 
                x = x + 2
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            elif int(dataSave[10]) > 15:
                x = x + 1
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            else:
                x = x + 0
                jsonLoad[dataSave[0]][dataSave[17]] = x    
            
            
            # Frequencia Cardiaca
            if int(dataSave[12]) > 120:
                x = x + 3
                jsonLoad[dataSave[0]][dataSave[17]] = x
            elif int(dataSave[12]) > 110: 
                x = x + 2
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            elif int(dataSave[12]) > 100:
                x = x + 1
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            else:
                x = x + 0
                jsonLoad[dataSave[0]][dataSave[17]] = x  
            
            
            # Saturacao Sanguinea
            if int(dataSave[14]) < 86:
                x = x + 3
                jsonLoad[dataSave[0]][dataSave[17]] = x
            elif int(dataSave[14]) < 90: 
                x = x + 2
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            elif int(dataSave[14]) < 93:
                x = x + 1
                jsonLoad[dataSave[0]][dataSave[17]] = x
                
            else:
                x = x + 0
                jsonLoad[dataSave[0]][dataSave[17]] = x  
            
            
            # Informa o Estado do paciente de acordo com os seus dados
            if x >= 5:
                jsonLoad[dataSave[0]][dataSave[15]] = 'Grave'
            elif x > 2:    
                jsonLoad[dataSave[0]][dataSave[15]] = 'Alerta'
            else:
                jsonLoad[dataSave[0]][dataSave[15]] = 'Estavel'
            
            # Ordena lista de atributos do JSON     
            ordered_items = sorted(jsonLoad.items(), key=lambda item: item[1]['Pontuacao'], reverse=True)
            
            # inicia conversao de list to OrderedDict
            ordered_ips_data_dict = OrderedDict(ordered_items)  
            
            # escreve o objeto atualizado no arquivo temporário
            j.dump(ordered_ips_data_dict, out, ensure_ascii=False, indent=4, separators=(',',':'))
    
    # sobreescreve o arquivo original com o temporario
    shutil.move(out.name, 'pacientes.json')