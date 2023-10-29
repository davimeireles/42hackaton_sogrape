#import da pasta com os respectivos sources
import scraping_files.continente
import scraping_files.el_corte_ingles
import scraping_files.garrafeira_soares

#EANS dos respectivos vinhos solicitados
ean_mateusrose = 5601012011500
ean_mateussparkling = 5601012001310
ean_trincabolotas = 5601012004427
ean_papafigos = 5601012011920

# chamada da funcao
scraping_files.continente.continente_scrap(5601012011500)
scraping_files.el_corte_ingles.el_corte_ingles_scrap(5601012004427)
scraping_files.garrafeira_soares.garrafeira_soares_scrap(5601012001310)