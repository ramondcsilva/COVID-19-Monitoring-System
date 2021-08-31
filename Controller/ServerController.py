import json, shutil, tempfile


def UpdateDataWriteJSON(data):
    dataSave = data.decode('utf-8').split(",")
    
    with open('pacientes.json', 'r+', encoding='utf-8') as arq, \
        tempfile.NamedTemporaryFile('w', delete=False) as out:
        # ler todo o arquivo e obter o objeto JSON
        jsonLoad = json.load(arq)
        
        arq.close()
        # atualizar os dados com a nova pergunta
        
        if dataSave[0] not in jsonLoad:
            y = {dataSave[0]: {
                    dataSave[1] : dataSave[2]
                    }
                }
            
            jsonLoad.update(y) 
            json.dump(jsonLoad, out, ensure_ascii=False, indent=4, separators=(',',':'))
        else: 
            jsonLoad[dataSave[0]][dataSave[1]] = dataSave[2]    
            json.dump(jsonLoad, out, ensure_ascii=False, indent=4, separators=(',',':'))
        # escreve o objeto atualizado no arquivo temporário
    
    shutil.move(out.name, 'pacientes.json')      
    
def CheckCriticallPatient (data):
    dataSave = data.decode('utf-8').split(",")
    
    if dataSave[1] == "Saturacao Sanguinea" and dataSave[2] < 85:
        dataSave = dataSave+",True"
    else:
        dataSave = dataSave+",False"            
        