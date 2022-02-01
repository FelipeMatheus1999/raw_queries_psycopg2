from http import HTTPStatus

import psycopg2
from flask import Flask, request


def membros_route(app: Flask):
    @app.get("/membros")
    def get_membros():
        conn = psycopg2(host="localhost", database="membros_db", user="felipe", password="4RaB3L02d")

        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM membros;
        """)

        getting_data = cur.fetchall()

        FIELDNAMES = ["id", "nome", "cpf", "data_registro"]
        processed_data = [dict(zip(FIELDNAMES, row)) for row in getting_data]

        conn.commit()
        cur.close()
        conn.close()

        return {"data": processed_data}, HTTPStatus.OK


    @app.post("/membros")
    def create_membros():
        data = request.get_json()

        conn = psycopg2(host="localhost", database="membros_db", user="felipe", password="4RaB3L02d")
        cur = conn.cursor()

        user = (data["nome"], data["cpf"], data["data_registro"])
        query = 'INSERT INTO membro (nome, cpf, data_registro) VALUES (%s, %s, %s)'
        cur .execute(user, query)

        conn.commit()
        
        cur.close()
        conn.close()

        return {"message": "member created"}, HTTPStatus.CREATED
