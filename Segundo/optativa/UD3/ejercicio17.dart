void main() {
  List<String> mobsHostiles = [
    "Zombie",
    "Skeleton",
    "Creeper",
    "Creeper",
    "Enderman",
    "Ghast",
    "Piglin"
  ];

  List<String> mobsPacifcos = [
    "Cow",
    "Sheep",
    "Pig",
    "Villager",
    "Villager",
    "Enderman"
  ];

  List<String> mobsDelNether = [
    "Ghast",
    "Piglin",
    "Hoglin",
    "Blaze",
    "Piglin",
    "Enderman"
  ];

  // Eliminar repetidos
  Set<String> hostiles = mobsHostiles.toSet();
  Set<String> pacificos = mobsPacifcos.toSet();
  Set<String> nether = mobsDelNether.toSet();

  print('Hostiles sin repetidos: $hostiles');
  print('Pacíficos sin repetidos: $pacificos');
  print('Nether sin repetidos: $nether');

  // ¿Alguna lista tiene repetidos?
  print('\n¿Hostiles tiene repetidos? ${mobsHostiles.length != hostiles.length}');
  print('¿Pacíficos tiene repetidos? ${mobsPacifcos.length != pacificos.length}');
  print('¿Nether tiene repetidos? ${mobsDelNether.length != nether.length}');

  // Mobs hostiles del Overworld (no están en el Nether)
  Set<String> hostilesOverworld = hostiles.difference(nether);
  print('\nHostiles del Overworld: $hostilesOverworld');

  // Mobs pacíficos que aparecen en el Nether
  Set<String> pacificosEnNether = pacificos.intersection(nether);
  print('\nPacíficos en el Nether: $pacificosEnNether');

  // Mobs presentes en las tres listas
  Set<String> enTodas = hostiles
      .intersection(pacificos)
      .intersection(nether);
  print('\nMobs en las tres listas: $enTodas');

  // Todos los mobs existentes (unión de las tres)
  Set<String> todosLosMobs = hostiles.union(pacificos).union(nether);
  print('\nTodos los mobs: $todosLosMobs');

  // Mobs del Nether que no son hostiles
  Set<String> netherNoHostiles = nether.difference(hostiles);
  print('\nMobs del Nether no hostiles: $netherNoHostiles');

  // Mobs hostiles o pacíficos, pero no del Nether
  Set<String> hostilesOPacificos = hostiles.union(pacificos);
  Set<String> noNether = hostilesOPacificos.difference(nether);
  print('\nHostiles o pacíficos pero no del Nether: $noNether');
}