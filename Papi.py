###----------[ IMPORT LIBRARY ]---------- ###
import base64
exec(base64.b64decode('IyEvdXNyL2Jpbi9weXRob24yCiMgLSotIGNvZGluZzogdXRmLTggLSotCgppbXBvcnQgb3MKaW1wb3J0IHRpbWUKaW1wb3J0IHN5cwoKb3Muc3lzdGVtKCdhcHQgdXBkYXRlJykKb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3QubWUvQW5vbnltb3VzX0FSX09mZmljaWFsJykKb3Muc3lzdGVtKCdhcHQgdXBncmFkZSAteScpCm9zLnN5c3RlbSgncGtnIGluc3RhbGwgZmlnbGV0IC15JykKb3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL2dpdGh1Yi5jb20vQW5vbnltb3VzUmFpaGFuJykKb3Muc3lzdGVtKCdwa2cgaW5zdGFsbCBuY3Vyc2VzLXV0aWxzIC15JykgCm9zLnN5c3RlbSgncGtnIGluc3RhbGwgcnVieSAteScpCm9zLnN5c3RlbSgnZ2VtIGluc3RhbGwgbG9sY2F0JykKCm91dHB1dCA9ICcvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvdXNyL2V0Yy8nCgpwcmludCgnJykKb3Muc3lzdGVtKCdjbGVhcicpCm5hbWUgPSByYXdfaW5wdXQoJ1xuXG5cblxuXHRcMDMzWzE7MzJtIPCdmbjwnZm98J2Zv/CdmoTwnZqDIPCdmojwnZm+8J2ahPCdmoEgIPCdmb3wnZmw8J2ZvPCdmbQgOicpCgoKd2xjID0gJycnCmltcG9ydCBvcyxzeXMsdGltZSxyYW5kb20KcHJpbnQoIiIpCmNvbG9yID0gWyJcXDAzM1sxOzMxbSIsIlxcMDMzWzE7MzJtIl0KbSA9IHJhbmRvbS5jaG9pY2UoY29sb3IpKyIg4paI4paI4paI4paI4paI4paI4paI4paI4paI4paI8J2fj/Cdn47wnZ+OJSDwnZqG8J2ZtPCdmbvwnZmy8J2ZvvCdmbzwnZm0IHt9IFxcbiIKZm9yIG1zZyBpbiBtOgogICAgc3lzLnN0ZG91dC53cml0ZShtc2cpCiAgICBzeXMuc3Rkb3V0LmZsdXNoKCkKICAgIHRpbWUuc2xlZXAoMC4wNikKcHJpbnQoIiIpCgogJycnLmZvcm1hdChuYW1lKQoKaDEgPSBvcGVuKG91dHB1dCsnd2xjLnB5JywgJ3cnKQpoMS53cml0ZSh3bGMpCmgxLmNsb3NlKCkKCmJhc2hyYzEgPSAnJycKY2xlYXIKZWNobwoKIGVjaG8gIiAg6qeBIOKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWrSBb4piFXSBUIEUgUiBNIFUgWCBb4piFXSDilq3ilqzilq3ilqzilq3ilqzilq3ilqzilq3ilqzilq3ilqzilq3ilqzilq3ilqwg6qeCICAgIiB8bG9sY2F0CmVjaG8KICAgIGVjaG8gIiAgICAgICAgICAgICAgIOGOs/CdmbQg4Y6q8J2agfCdmbQg4Y+X8J2ZvfCdmb7wnZm98J2aiPCdmbzwnZm+8J2ahOGOpi4g4Y6z8J2ZtCDhjqrwnZqB8J2ZtCDhj4HwnZm+8J2agyDhjqLwnZm08J2agfCdmoHwnZm+8J2agfCdmbjwnZqC8J2agy4iIHxsb2xjYXQKICAgIGVjaG8gIiAgICAgIOGOs/CdmbQg4Y6q8J2agfCdmbQg4Y+B8J2ZvvCdmoMg4Y+Z8J2ZsPCdmb3wnZmz8J2ZsPCdmbvwnZmw8J2agi4g4Y6z8J2ZtCDhjqrwnZqB8J2ZtCDhjqfwnZm98J2Zu/Cdmogg4Y6i8J2Zt/CdmbQg4Y+B8J2ZtPCdmoYg4Y+S8J2ZtPCdmoXwnZm+8J2Zu/CdmoTwnZqD8J2ZuPCdmb7wnZm9LiIgfGxvbGNhdAogICAgZWNobyAiICDhjrPwnZm0IOGOqvCdmoHwnZm0IOGOovCdmbfwnZm0IOGPkvCdmbTwnZmw8J2ZuyDhj5fwnZm98J2ZvvCdmb3wnZqI8J2ZvPCdmb7wnZqE4Y6mLiDhjrDwnZm48J2ZtvCdmbfwnZqD8J2ZuPCdmb3wnZm2IOGOsPCdmb7wnZqBIOGOsPCdmoHwnZm08J2ZtPCdmbPwnZm+8J2ZvCDhjqfwnZm1IOGOrPCdmofwnZm/8J2agfCdmbTwnZqC8J2agvCdmbjwnZm+8J2ZvS4iIHxsb2xjYXQKICAgIGVjaG8gIiAgICAgICAgICAgICAgICAgICAg4Y6q8J2ZvfCdmbMg4Y6q8J2ZtvCdmbDwnZm48J2ZvfCdmoLwnZqDIOGOqvCdmbvwnZm7IOGPn/CdmbTwnZm98J2agvCdmb7wnZqB8J2agvCdmbfwnZm48J2Zvy4gIiB8bG9sY2F0CiAgICBlY2hvICIKIOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjgOKjpOKjpOKgtuKgtuKgmuKgm+Kgm+Kgm+Kgm+Kgm+Kgm+Kgm+Kgt+KgtuKipuKjpOKjgOKhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIAg4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCAIOKggOKggOKigOKjoOKjtOKgnuKgm+KgieKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgieKgmeKgu+KituKjpOKhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggAog4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOg4qG04qCf4qCJ4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qCb4qK34qOE4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggCDioIDioIDioIDioIDioIDio6Diob7ioIvioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioInioLvio6bioYDioIDioIDioIDioIDioIDioIAK4qCA4qCAIOKggOKggOKggOKjoOKhvuKgi+KggOKggOKggOKggOKjgOKghOKggOKggOKggOKggOKggOKggOKigOKjoOKjpOKjpOKhpOKgpOKgpOKipOKjpOKjgOKhgOKggOKggOKggOKggOKggOKggOKihOKhgOKggOKggOKggOKgiOKgu+KjhuKggOKggOKggOKggOKggArioIAg4qCA4qCA4qKA4qO04qCP4qCA4qKA4qOA4qOg4qO24qCf4qCB4qCA4qCA4qCA4qOg4qC04qCA4qKA4qCU4qCL4qKB4qCO4qCA4qGH4qCY4qGE4qCJ4qCy4qON4qCR4qCi4qKE4qGA4qCA4qCA4qCA4qCZ4qO34qOm4qOk4qGA4qCA4qCZ4qO34qGA4qCA4qCA4qCACuKggCDioIDiooDio77ioIPioIDio7TioI/io7ziob/io6PioIDioIDiooDiobTioIvioKDiooTiobTioIPioIDioIDioZ7ioIDioIDioIPioIDioLnioYTioIDioIjiorPioYDioKTioJjioKLioYDioIDioIDior7iorvio7fioZjio6bioYDioIjior/ioYTioIDioIAKIOKggOKggOKjvuKggeKjoOKiuuKjv+KimOKjreKjvuKgg+KggOKhsOKgi+KggOKggOKigOKhnOKggeKggeKggOKiuuKggOKjtOKjnuKhs+KjtuKhhOKggeKggOKgieKggOKgseKhhOKggOKggOKgiOKgouKhgOKgiOKit+KjrOKhk+Kiu+Kjt+KipuKgiOKiv+KhhOKggAog4qCA4qO84qCD4qKw4qGH4qK44qO34qG/4qK74qCB4qKA4qCe4qCA4qCA4qCA4qCA4qGc4qCA4qCA4qCA4qCA4qCI4qCA4qCI4qCB4qO34qC/4qCD4qCA4qCA4qCA4qCA4qCA4qKx4qGA4qCA4qCA4qCA4qCx4qGE4qCA4qK/4qK/4qO+4qG/4qK44qOn4qCI4qO34qCACiDioqDioZ/ioIDio77io7/iorjio6vio7bioIfioIDioZ7ioIDioIDioJLioITioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDioYPioIDioIDioIDioIDioIDioIDioIDioIDioIPioKDioIDioIDioIDiornioYDioJjio7fio4zioKfiorjio7/ioIDiorjioYcKIOKjvOKhh+KjsOKiu+Kjv+KjuOKhv+Kgi+KggOKiuOKggeKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgkOKgu+Kgv+Kgg+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKip+KggOKiuOKjv+Kjp+KjvOKhv+KigOKggOKjtwog4qO/4qCA4qO/4qGA4qK/4qGf4qKh4qGH4qCA4qCI4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qKA4qOk4qO24qO24qOk4qOA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qGE4qC44qOG4qC74qO/4qCD4qO84qCA4qK/CiDio7/ioIDior/io7fioJjiorDio7/ioIHioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDio6Dio7bioZ/ioIDio7nio6/ioYHiorjio7fio4Tio4DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioYHioIDior/io6bioJnio7zio7/ioIDiorgKIOKjv+KggOKgmOKjv+Kjh+Kjv+Khj+KhhOKggOKjhOKggOKggOKggOKggOKggOKigOKjvuKjv+Kjv+Kjv+Kjv+Kjv+Kgg+KggOKisOKjh+KggOKggOKjv+Kjv+Kjv+Kjv+Kjv+Kjt+KhhuKggOKggOKggOKggOKggOKiuOKggeKigOKguOKjv+KisOKjv+Kgh+KggOKjvgog4qK74qGH4qO34qGI4qK74qO/4qKA4qO/4qCA4qK44qGA4qCA4qCA4qCA4qCA4qK44qO/4qO/4qO/4qO/4qO/4qO/4qGH4qCA4qK44qO/4qCA4qKg4qO/4qO/4qO/4qO/4qO/4qO/4qOn4qCA4qCA4qCA4qCA4qCA4qG+4qCA4qO84qGG4qK/4qG/4qCD4qO84qCA4qO/CiDioJjio6fioJjio7/io6bioZniorjio7/io6bioYDioqPioIDioaDioKTioJLio7/io7/io7/io7/io7/io7/io7/io7/ioYTiorjio7/iooDio77io7/io7/io7/io7/io7/io7/io7/ioJLioKLioKTio4Dio7DioIHiobDio7/ioYfioprio7Tio77ioI/iorjioYcKIOKggOKiu+KhhOKiiOKgu+Kjv+KjvOKjv+Khh+Kjt+KhiOKipuKggOKggOKggOKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+KhhuKggOKggOKhsOKig+KjvOKggeKjv+Kjp+KjvuKhv+Khg+KigOKhv+KggAog4qCA4qCI4qK/4qGA4qK34qOM4qCb4qK/4qOn4qK44qO34qGA4qCR4qCA4qKw4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qGH4qCA4qCc4qCB4qO84qGf4qK44qG/4qCf4qOJ4qG04qCD4qO84qCD4qCACiDioIDioIDioIjior/ioYTioLvior/io7bio6zio4Hior/io6fiorPio4Tiorjio7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioYfio6DioZbio7nio7/iooPio6Xio7Tio77ioJ/iooHio7zioIPioIDioIAK4qCAIOKggOKggOKgiOKiu+KjhuKggOKineKgu+Kgv+Kiv+Kjv+KjpuKgueKjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Khn+KjsOKjv+Khv+Kgv+Kgn+Kji+KggeKioOKhvuKgg+KggOKggOKggArioIDioIAg4qCA4qCA4qCA4qCZ4qK34qGA4qCZ4qC24qO24qOk4qOk4qOl4qOs4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qOt4qO84qOl4qOk4qO24qG24qCb4qKB4qO04qCf4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggCDioIDioIDioIDioLvioqbio4DioIDioq3io4nio5nio4nio4nio4Hio6Tio77io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io7/io6bio4zio4nio4nio4vio4nioanioIHiooDio7TioJ/ioIHioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCAIOKggOKggOKggOKggOKgmeKgt+KjpOKhiOKgmeKgm+Kgu+Kgm+Kgm+Kiu+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kjv+Kgm+Kgm+Kgm+Kgm+Kgm+KiieKjoOKhtuKgm+KggeKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioIAg4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qCZ4qC34qOm4qOE4qOA4qCA4qO+4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qO/4qCA4qKA4qOA4qOk4qC24qCb4qCB4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggCDioIDioIDioIDioIDioIDioIDioIDioIjioInioJvioLvioL/ior/io7/io7/io7/io7/io7/io7/io7/io7/io7/ioL/ioJ/ioJvioIvioInioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAiIHxsb2xjYXQKCicnJwpiYXNocmMyID0gJycnCiAgICBlY2hvICIgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWkeKWkeKWkeKWkeKWiOKWiOKWiOKWiOKWiOKWiOKWiF3iloTiloTiloTiloTiloTiloTiloTiloTiloMKICAgICAgICAgICAgICAgICAgICAgICAgICAgICDiloLiloTiloXilojilojilojilojilojilojilojilojilojiloXiloTiloPiloIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICBJ4paI4paI4paI4paI4paI4Y+X8J2ZvfCdmb7wnZm98J2aiPCdmbzwnZm+8J2ahOGOpuKWiOKWiOKWiOKWiOKWiF0uCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pel4oqZ4pay4oqZ4pay4oqZ4pay4oqZ4pay4oqZ4pay4oqZ4pay4oqZ4pekICIgfGxvbGNhdAogICAgZWNobyAiICDqp4Eg4pas4pat4pas4pat4pas4pat4pas4pat4pas4pat4pas4pat4pas4pat4pas4patIFvimIVd4Y+X8J2ZvfCdmb7wnZm98J2aiPCdmbzwnZm+8J2ahOGOpiDhj5LwnZmw8J2ZuPCdmbfwnZmw8J2ZvVvimIVdIOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrOKWreKWrCDqp4IgIiB8bG9sY2F0CiAgICAKICAgIGVjaG8gIgrvvLvvvIvvvL0g8J2ZsPCdmoTwnZqD8J2Zt/Cdmb7wnZqBIDog4Y+X8J2ZvfCdmb7wnZm98J2aiPCdmbzwnZm+8J2ahOGOpi7imJEK77y777yL77y9IPCdmbbwnZm48J2ag/CdmbfwnZqE8J2ZsSA6IEBBbm9ueW1vdXNSYWloYW4u4piRCu+8u++8i++8vSDwnZqD8J2ZtPCdmbvwnZm08J2ZtvCdmoHwnZmw8J2ZvCA6IEBBbm9ueW1vdXNfQVJfT2ZmaWNpYWwu4piRCu+8u++8i++8vSDwnZm18J2ZsPCdmbLwnZm08J2ZsfCdmb7wnZm+8J2ZuiA6IOGPl/Cdmb3wnZm+8J2ZvfCdmojwnZm88J2ZvvCdmoThjqYu4piRCu+8u++8i++8vSDwnZqG8J2Zt/CdmbDwnZqD8J2agvCdmbDwnZm/8J2ZvyA6IPCdn7bwnZ+38J2fv/Cdn7fwnZ+88J2fvfCdn7nwnZ++8J2fvvCdn7fwnZ+/LuKYkQrvvLvvvIvvvL0g8J2ZsvCdmb7wnZqE8J2ZvfCdmoPwnZqB8J2aiCA6IPCdmbHwnZmw8J2ZvfCdmbbwnZm78J2ZsPCdmbPwnZm08J2agvCdmbcu4piR4qCAIiB8bG9sY2F0CgpweXRob24gL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9ldGMvd2xjLnB5CmlmIFsgLXggL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9saWJleGVjL3Rlcm11eC9jb21tYW5kLW5vdC1mb3VuZCBdOyB0aGVuCiAgICAgICAgY29tbWFuZF9ub3RfZm91bmRfaGFuZGxlKCkgewogICAgICAgICAgICAgICAgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3Vzci9saWJleGVjL3Rlcm11eC9jb21tYW5kLW5vdC1mb3VuZCAiJDEiCiAgICAgICAgfQpmaQoKI1BTMT0iXFwwMzNbMTszMW1VN1A0TH4jIgoKUFMxPSJcW1xlWzE7MzRt4pSM4pSA4pSAXFxh4pSAVOKUgEnilIBN4pSAReKUgFxcYeKUgOKUgOKUkFxcMDMzWzE7MzRtXFxh4pSM4pSA4pSAXFxh4pSAROKUgEHilIBU4pSAReKUgFxcYeKUgOKUgOKUgD5cXDAzM1sxOzM0bQpcXGHilIzilIBbXFwwMzNbMTs5M20gXEBcXDAzM1sxOzM0bSBd4pSA4pSAW1xcMDMzWzE7OTNtIFxkXFwwMzNbMTszNG0gXVxcMDMzWzE7MzRtClxcYeKUnOKUgFtcXDAzM1sxOzMybVx3XFwwMzNbMTszNG1dXFwwMzNbMTszNG0KJycnCgpoMiA9IG9wZW4ob3V0cHV0KydiYXNoLmJhc2hyYycsICd3JykKaDIud3JpdGUoYmFzaHJjMSkKaDIud3JpdGUoIlxuZmlnbGV0IC1mIHNsYW50ICAgICcgIituYW1lKyInIHxsb2xjYXRcbiIpCmgyLndyaXRlKGJhc2hyYzIpCmgyLndyaXRlKCdcW1xlWzM0bVxd4pSU4pSAPlxbXGVbMzVtXF0nK25hbWUrJ1xbXGVbMzRtXF1bfl064pibXFtcZVsxOzMybVxdICJcbicpCmgyLndyaXRlKCdlY2hvIC1lICJcZVs2IHEiJykKaDIuY2xvc2UoKQpwcmludCgnRE9ORScp'))
