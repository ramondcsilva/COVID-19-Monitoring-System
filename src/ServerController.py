import json as j, shutil, tempfile


def UpdateDataWriteJSON(data):
    # variavel que salva o id do paciente
    dataSave = data.decode('utf-8').split(",")
    
    #inicia a escrito no documento JSON
    with open('pacientes.json', 'r+', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        
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
                    dataSave[15] : dataSave[16]
                    }
                }
    
            jsonLoad.update(y) 
            j.dump(jsonLoad, out, ensure_ascii=False, indent=4, separators=(',',':'))
            jsonLoad = '';
        else: 
            # atualizar os dados do paciente conectado
            jsonLoad[dataSave[0]][dataSave[1]] = dataSave[2]
            jsonLoad[dataSave[0]][dataSave[3]] = dataSave[4]
            jsonLoad[dataSave[0]][dataSave[5]] = dataSave[6]
            jsonLoad[dataSave[0]][dataSave[7]] = dataSave[8]
            jsonLoad[dataSave[0]][dataSave[9]] = dataSave[10]
            jsonLoad[dataSave[0]][dataSave[11]] = dataSave[12]
            jsonLoad[dataSave[0]][dataSave[13]] = dataSave[14]
            
            # Informa o Estado do paciente de acordo com os seus dados
            if int(dataSave[8]) < 100:
                jsonLoad[dataSave[0]][dataSave[15]] = 'Grave'
            elif int(dataSave[10]) > 14:    
                jsonLoad[dataSave[0]][dataSave[15]] = 'Grave'
            elif int(dataSave[12]) > 100:    
                jsonLoad[dataSave[0]][dataSave[15]] = 'Grave'
            elif int(dataSave[14]) < 92:    
                jsonLoad[dataSave[0]][dataSave[15]] = 'Grave'
            elif int(dataSave[6]) > 37:    
                jsonLoad[dataSave[0]][dataSave[15]] = 'Febril'
            else:
                jsonLoad[dataSave[0]][dataSave[15]] = 'Estavel'
            j.dump(jsonLoad, out, ensure_ascii=False, indent=4, separators=(',',':'))
        # escreve o objeto atualizado no arquivo temporário
    
    # sobreescreve o arquivo original com o temporario
    shutil.move(out.name, 'pacientes.json')