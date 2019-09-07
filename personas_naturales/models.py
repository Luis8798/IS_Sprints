from django.db import models
import datetime

# Create your models here.

class Persona_Natural(models.Model):

	c = [("Alamor","Alamor"),("Alausí","Alausí"),("Amaluza","Amaluza"),("Ambato","Ambato"),("Arajuno","Arajuno"),("Archidona","Archidona"),("Arenillas","Arenillas"),("Atacames","Atacames"),("Atuntaquí","Atuntaquí"),("Azogues","Azogues"),("Baba","Baba"),("Babahoyo","Babahoyo"),("Baeza","Baeza"),("Bahía de Caráquez","Bahía de Caráquez"),("Balao","Balao"),("Balsas","Balsas"),("Balzar","Balzar"),("Baños de Agua Santa","Baños de Agua Santa"),("Biblián","Biblián"),("Bolívar","Bolívar"),("Bucay","Bucay"),("Buena Fe","Buena Fe"),("Cajabamba","Cajabamba"),("Calceta","Calceta"),("Caluma","Caluma"),("Camilo Ponce Enríquez","Camilo Ponce Enríquez"),("Cariamanga","Cariamanga"),("Carlos Julio Arosemena Tola","Carlos Julio Arosemena Tola"),("Catacocha","Catacocha"),("Catamayo","Catamayo"),("Catarama","Catarama"),("Cayambe","Cayambe"),("Cañar","Cañar"),("Celica","Celica"),("Cevallos","Cevallos"),("Chaguarpamba","Chaguarpamba"),("Chambo","Chambo"),("Chilla","Chilla"),("Chillanes","Chillanes"),("Chimbo","Chimbo"),("Chone","Chone"),("Chordeleg","Chordeleg"),("Chunchi","Chunchi"),("Cnel. Marcelino Maridueña","Cnel. Marcelino Maridueña"),("Colimes","Colimes"),("Cotacachi","Cotacachi"),("Cuenca","Cuenca"),("Cumandá","Cumandá"),("Daule","Daule"),("Durán","Durán"),("Déleg","Déleg"),("Echendía","Echendía"),("El Carmen","El Carmen"),("El Chaco","El Chaco"),("El Corazón","El Corazón"),("El Dorado de Cascales","El Dorado de Cascales"),("El Guabo","El Guabo"),("El Pan","El Pan"),("El Pangui","El Pangui"),("El Tambo","El Tambo"),("El Triunfo","El Triunfo"),("El Ángel","El Ángel"),("Esmeraldas","Esmeraldas"),("Flavio Alfaro","Flavio Alfaro"),("Girón","Girón"),("Gonzanamá","Gonzanamá"),("Guachapala","Guachapala"),("Gualaceo","Gualaceo"),("Gualaquiza","Gualaquiza"),("Guamote","Guamote"),("Guano","Guano"),("Guaranda","Guaranda"),("Guayaquil","Guayaquil"),("Guayzimi","Guayzimi"),("Huaca","Huaca"),("Huamboya","Huamboya"),("Huaquillas","Huaquillas"),("Ibarra","Ibarra"),("Ididrio Ayora","Ididrio Ayora"),("Jama","Jama"),("Jaramijó","Jaramijó"),("Jipijapa","Jipijapa"),("Jujan","Jujan"),("Junín","Junín"),("La Bonita","La Bonita"),("La Concordia","La Concordia"),("La Joya de los Sachas","La Joya de los Sachas"),("La Libertad","La Libertad"),("La Maná","La Maná"),("La Troncal","La Troncal"),("La Victoria","La Victoria"),("Las Naves","Las Naves"),("Latacunga","Latacunga"),("Limones","Limones"),("Limón","Limón"),("Logroño","Logroño"),("Loja","Loja"),("Lomaas de Sargentillo","Lomaas de Sargentillo"),("Loreto","Loreto"),("Lumbaqui","Lumbaqui"),("Macará","Macará"),("Macas","Macas"),("Machachi","Machachi"),("Machala","Machala"),("Manta","Manta"),("Marcabelí","Marcabelí"),("Mera","Mera"),("Milagro","Milagro"),("Mira","Mira"),("Mocache","Mocache"),("Mocha","Mocha"),("Montalvo","Montalvo"),("Montecristi","Montecristi"),("Muisne","Muisne"),("Nabón","Nabón"),("Naranjal","Naranjal"),("Naranjito","Naranjito"),("Nobol","Nobol"),("Nueva Loja","Nueva Loja"),("Nuevo Rocafuerte","Nuevo Rocafuerte"),("Olmedo","Olmedo"),("Olmedo","Olmedo"),("Otavalo","Otavalo"),("Oña","Oña"),("Pablo Sexto","Pablo Sexto"),("Paccha","Paccha"),("Paján","Paján"),("Palanda","Palanda"),("Palenque","Palenque"),("Palestina","Palestina"),("Pallatanga","Pallatanga"),("Palora","Palora"),("Paquisha","Paquisha"),("Pasaje","Pasaje"),("Patate","Patate"),("Paute","Paute"),("Pedernales","Pedernales"),("Pedro Carbo","Pedro Carbo"),("Pedro Vicendo Maldonado","Pedro Vicendo Maldonado"),("Pelileo","Pelileo"),("Penipe","Penipe"),("Pichincha","Pichincha"),("Pimampiro","Pimampiro"),("Pindal","Pindal"),("Piñas","Piñas"),("Playas","Playas"),("Portovelo","Portovelo"),("Portoviejo","Portoviejo"),("Pucará","Pucará"),("Puebloviejo","Puebloviejo"),("Puerto Ayora","Puerto Ayora"),("Puerto Bauerizo Moreno","Puerto Bauerizo Moreno"),("Puerto Francisco de Orellana","Puerto Francisco de Orellana"),("Puerto López","Puerto López"),("Puerto Quito","Puerto Quito"),("Puerto Villamil","Puerto Villamil"),("Pujulí","Pujulí"),("Putumayo","Putumayo"),("Puyo","Puyo"),("Píllaro","Píllaro"),("Quero","Quero"),("Quevedo","Quevedo"),("Quinindé","Quinindé"),("Quinsaloma","Quinsaloma"),("Quito","Quito"),("Riobamba","Riobamba"),("Rioverde","Rioverde"),("Rocafuerte","Rocafuerte"),("Salcedo","Salcedo"),("Salinas","Salinas"),("Salitre","Salitre"),("Samborondón","Samborondón"),("Samn Fernando","Samn Fernando"),("San Gabriel","San Gabriel"),("San Juan Bosco","San Juan Bosco"),("San Lorenzo","San Lorenzo"),("San Miguel","San Miguel"),("San Miguel de los Bancos","San Miguel de los Bancos"),("San Vicente","San Vicente"),("Sangolquí","Sangolquí"),("Santa Ana","Santa Ana"),("Santa Clara","Santa Clara"),("Santa Elena","Santa Elena"),("Santa Isabel","Santa Isabel"),("Santa Lucía","Santa Lucía"),("Santa Rosa","Santa Rosa"),("Santiago","Santiago"),("Santiago de Méndez","Santiago de Méndez"),("Santo Domingo","Santo Domingo"),("Saquisilí","Saquisilí"),("Saraguro","Saraguro"),("Sevilla de Oro","Sevilla de Oro"),("Shushufinfi","Shushufinfi"),("Sigchos","Sigchos"),("Simón Bolívar","Simón Bolívar"),("Sorozanga","Sorozanga"),("Sucre","Sucre"),("Sucúa","Sucúa"),("Suscal","Suscal"),("Sígsig","Sígsig"),("Tabacundo","Tabacundo"),("Taisha","Taisha"),("Tarapoa","Tarapoa"),("Tena","Tena"),("Tiputini","Tiputini"),("Tisaleo","Tisaleo"),("Tosagua","Tosagua"),("Tulcán","Tulcán"),("Urcuquí","Urcuquí"),("Valencia","Valencia"),("Velasco Ibarra","Velasco Ibarra"),("Ventanas","Ventanas"),("Vinces","Vinces"),("Yacuambi","Yacuambi"),("Yaguachi","Yaguachi"),("Yantzaza","Yantzaza"),("Zamora","Zamora"),("Zapotillo","Zapotillo"),("Zaruma","Zaruma"),("Zumba","Zumba"),("Zumbi","Zumbi")]
	for_trabajo = [("Dependiente","Dependiente"), ("Independiente","Profesional Independiente")]
	estudios = [("Primaria","Primaria"), ("Secundaria","Secundaria"), ("Tercer Nivel","Tercer Nivel"), ("Postgrado","Postgrado")]

	cedula = models.CharField(max_length=10, primary_key=True, verbose_name="Cédula")
	apellidos = models.CharField(max_length=75)
	nombres = models.CharField(max_length=75)
	fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", help_text="AAAA-MM-DD")
	tel_domicilio = models.CharField(max_length=10, blank=True, null=True, verbose_name="Teléfono Domicilio")
	celular = models.CharField(max_length=10,blank=True, null=True)
	email = models.EmailField(max_length=254,blank=True, null=True)
	ci_domicilio = models.CharField(choices=c, max_length=100, verbose_name="Ciudad Domicilio")
	dir_domicilio = models.CharField(max_length=75, verbose_name="Dirección Domicilio")
	nivel_estudio = models.CharField(choices=estudios, default="Primaria", max_length=50, verbose_name="Nivel de Estudio")
	ti_tercernivel = models.CharField(max_length=100, blank=True, null=True, verbose_name="Título Tercer Nivel")
	un_tercernivel = models.CharField(max_length=75, blank=True, null=True, verbose_name="Universidad Tercer Nivel")
	ti_cuartonivel = models.CharField(max_length=100, blank=True, null=True, verbose_name="Titulo Cuarto Nivel")
	un_cuartonivel = models.CharField(max_length=75, blank=True, null=True, verbose_name="Universidad Cuarto Nivel")
	profesion = models.CharField(max_length=100, blank=True, null=True)
	forma_trabajo = models.CharField(choices=for_trabajo, blank=True, null=True, max_length=100, verbose_name="Forma de Trabajo")
	empresa = models.CharField(max_length=75, blank=True, null=True)
	cargo = models.CharField(max_length=50, blank=True, null=True)
	ci_trabajo = models.CharField(choices=c, max_length=100, blank=True, null=True, verbose_name="Ciudad Trabajo")
	area = models.CharField(max_length=50, blank=True, null=True, verbose_name="Área/Departamento")
	dir_trabajo = models.CharField(max_length=75, blank=True, null=True, verbose_name="Dirección Trabajo")
	tel_trabajo = models.CharField(max_length=10, blank=True, null=True, verbose_name="Teléfono Trabajo")
	red_social = models.CharField(max_length=50, verbose_name="Red Social por donde se enteró de este evento")
