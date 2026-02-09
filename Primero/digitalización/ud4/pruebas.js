function empiezanPorA(lista) {
    let resultado = [];

    for (let palabra of lista) {
        if (palabra.startsWith("a")) {
            resultado.push(palabra);
        }
    }

    return resultado;
}
