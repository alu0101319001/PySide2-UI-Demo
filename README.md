# Demo UI with Pyside2

## Version 1 : Interfaz gráfica
En una primera versión, realicé una demo de interfaz gráfica, en que se representaba distintas salas de ordenadores. En cada sala (visibles en forma de tabulaciones), se encuentra un grid de Pcs, cuyo icono indica el estado actual del mismo. Con click derecho en cada icono, abre un menú desplegable de opciones a ejecutar en dicho PC. 

A la izquierda, se despliega una sidebar que contiene diferentes opciones a ejecutar en todos los ordenadores de la sala de forma simultánea. 

### Componentes Principales:
- PCs: cada PC es representado por la clase PcWidget.
- Rooms: con la clase RoomWidget, se crea un grid de todos los PC disponibles en dicha sala.
- Zone: en la clase PcZone se representa las tabulaciones que permite seleccionar cada room.
- Section: en la clase SectionWidget se define una serie catagorizada de opciones.
- Sidebar: en la clase SidebarWidget se reunen todas las secciones y opciones a aplicar en la room visualizada.
- MainWindow: en la clase ControlCommandView se integra todos estos widgets mencionados.

## Version 2 : Integración de una BBDD y un proceso de autenticación [Work In Progress]
En la segunda versión, se ha creado una base de datos sobre la que sostener la interfaz gráfica y extraer la información necesaria. Además, de incorporar a la aplicación un sistema de autenticación.

__[Work In Progress]__ : Se ha terminado de implementar la BBDD y conectarla al sistema de autenticación. Ahora quedería modificar los componentes de la _Versión 1_ para aplicar el uso de la BBDD. También, queda por implementar la ventana de Perfil de usuario y la gestión de sesiones. 

### Componentes Principales:
- Schema: en el fichero schema.sql se muestra las consultas usadas para definir las 3 tablas usadas actualmente -> user, computer y access. 
- Bbdd: en el archivo bbdd.py se encuentra toda la implementación de la base de datos, concentrada en la clase DatabaseManager.
- Authentication: se han creado dos widgets: Login y Register para realizar dichos procesos. Conectados actualmente con la BBDD.
