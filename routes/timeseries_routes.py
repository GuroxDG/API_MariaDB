from fastapi import APIRouter, Path
from sqlalchemy import text
from enum import Enum
from cryptography.fernet import Fernet
from config.plugMariaDB import conn
from models.timeSeries import timeSeries
from schemas.timeSeries import TimeSeries, ExchageFX, Query
from utils.get_data import insertData

from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get('/')
async def hellow_world():
    return {'hellow word'}

@user.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {'id':id}

@user.get('/license-plates/{license}')
async def get_license_plate(license : str = Path(..., regex=r'^7\w{2}-\d{3}-\w{2}$')):
    return {'license':license}

@user.get("/users_db/{val}",response_model=List[TimeSeries])
def get_user(val: str):
    result = conn.execute(timeSeries.select().where(timeSeries.c.from_symbol == val))
    return result

@user.post('/query', response_model=list[TimeSeries])
def select_query(query: Query):
    consulta = query.query
    print(consulta)
    result = conn.execute(text(consulta)).fetchall( )
    return result

@user.post('/h')
def insert_info(data: ExchageFX):
    return insertData(data)

@user.get('/prueba')
def insert_info():
    valor = {"status":"Success",
             "response":[["CODIGO","NOMBRE","SNAME","TIPO","NUME","DRIVER","UNIDAD","SECT","CLUS","POSI","CODIGOCONTABLE","DESCRIPCION","CENTRO","CENTRO2","CENTRO3","VALOR","VALOR2","VALOR3","VALOR4","VALOR5","VALOR6","VALOR7","VALOR8","VARTYPE","VARTYPE_R","UNIR","TUNI","DIRECTOS","INDIRECTOS","TOTAL","DIRE_ING","INDI_ING","TOTA_ING","COSTOINI","INGRFP","TOTALF","TOTALV","TOTALS","ITOTALF","ITOTALV","ITOTALS","PRESUPUESTO","CAPREA","CAPREA2","CAPREA3","CAPREA4","ESTADINA","ESDIES","ESINVEN","ESTERM","ULAS","SAAN","PROD","COMP","DESP","RECI","DISP","VEND","CONS","BAJA","SALD","INGR","MOV1","MOV2","CAPA","ESTA","TDIS","VARI","COD_REC","ACUMUE","RECDIS","CAPREC","UNISTD","TOTSTD","AUTCAL","TMUERTOS","RESO","RESO2","DATM","NOIN","GRUP","DRIV","KTYPE","KLEA","KLEAM","KLEAS","KOUT","KOUTM","KOUTS","KOUTF","KVA","KIT","CUSTOM1","CUSTOM2","VALOR9","VALOR10","VNAME","VNAME2","VNAME3","VNAME4","VNAME5","VNAME6","VNAME7","VNAME8","VNAME9","VNAME10"],["ACT-ADM-100-01","Financials","","ACTIVITY","1.0","","UNI","INSTITUTIONAL MANAGEMENT","","8007.0","","","100","","","","","","","","","","","F","","","","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","","","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","","","","","0.0","0.0","0.0","0.0","","0.0","","","0.0","","FINAN","","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-100-02","Corporative","","ACTIVITY","2.0","","UNI","INSTITUTIONAL MANAGEMENT","","9007.0","","","100","","","","","","","","","","","F","","","","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","1","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","CORP","","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-01","Plan Audit","","ACTIVITY","3.0","","UNI","INTERNAL AUDIT","","13008.0","","","101","","","","","","","","","","","F","F","","","0.0","8059.38651562149","8059.38651562149","0.0","0.0","0.0","0.0","0.0","8059.38651562149","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","1","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-02","Execute Audit","","ACTIVITY","4.0","","UNI","INTERNAL AUDIT","","14008.0","","","101","","","","","","","","","","","F","F","","","61134.14628","8547.83418323492","69681.9804632349","0.0","0.0","0.0","0.0","0.0","69681.9804632349","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-101-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-03","Execute Audit Report","","ACTIVITY","5.0","","UNI","INTERNAL AUDIT","","15008.0","","","101","","","","","","","","","","","F","F","","","89959.646724","6838.26734658793","96797.9140705879","0.0","0.0","0.0","0.0","0.0","96797.9140705879","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-101-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-04","Follow-Up Action Plans","","ACTIVITY","6.0","","UNI","INTERNAL AUDIT","","16008.0","","","101","","","","","","","","","","","F","F","","","0.0","5861.37201136108","5861.37201136108","0.0","0.0","0.0","0.0","0.0","5861.37201136108","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-101-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-05","Participate In Audit Committee","","ACTIVITY","7.0","","UNI","INTERNAL AUDIT","","17008.0","","","101","","","","","","","","","","","F","F","","","0.0","6105.5958451678","6105.5958451678","0.0","0.0","0.0","0.0","0.0","6105.5958451678","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-101-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-101-06","Participate In Disclaimer Committee","","ACTIVITY","8.0","","UNI","INTERNAL AUDIT","","18008.0","","","101","","","","","","","","","","","F","F","","","0.0","7815.16268181478","7815.16268181478","0.0","0.0","0.0","0.0","0.0","7815.16268181478","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-101-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-102-01","Execute Post Medical Administrative Audit","","ACTIVITY","9.0","","UNI","MEDICAL AUDIT","","5008.0","","","102","","","","","","","","","","","F","F","","","0.0","440204.234777135","440204.234777135","0.0","0.0","0.0","0.0","0.0","440204.234777135","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","1","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"],["ACT-ADM-102-02","Execute Concurrent Medical Audit","","ACTIVITY","10.0","","UNI","MEDICAL AUDIT","","6008.0","","","102","","","","","","","","","","","F","F","","","0.0","353544.832246118","353544.832246118","0.0","0.0","0.0","0.0","0.0","353544.832246118","0.0","0.0","0.0","0.0","0.0","0.0","1.0","0.0","0.0","0.0","F","F","F","F","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","","34","","","","0.0","0.0","0.0","0.0","F","0.0","F","F","0.0","","","ACT-ADM-102-01,","","0.0","","","0.0","","","","0.0","0.0","","","null","null","null","null","null","null","null","null","null","null","null","null"]]}
    return valor