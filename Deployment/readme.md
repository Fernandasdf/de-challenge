## Deployment 

El deployment del etl se realiza mediante una imagen docker, la cual es pública en mi repositorio en Docker Hub. Como requisito, se debe tener instalado docker en el ambiente donde se hará el despliegue.

- comando para descargar imagen:
`docker pull fernandasdf/fer-de-challenge:latest`

- comando para ejecutar etl
`docker run -v <path-to-de-challenge>\src:/src fer-de-challenge`
donde <path-to-de-challenge> es el directorio raíz del proyecto (local)
 
- reporte final es un archivo excel y se encuentra en src\games_report.xlsx
  