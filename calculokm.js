import React, { useState } from 'react';
import { StyleSheet, Text, View,
TextInput, TouchableOpacity, Alert }
from 'react-native';

export default function App() {
const [km, setKm] = useState('');
const [metros, setMetros] = useState(null);

const handleConvert = () => {
// Verifica se o campo de entrada não está vazio
if (km === '') {
Alert.alert('Erro', 'Por favor, digite um valor em quilômetros.');
return;
}

// Converte a string para um número
const valorEmKm = parseFloat(km);

if (isNaN(valorEmKm)) {
Alert.alert('Erro', 'Por favor, digite um número válido.');
return;
}

// Realiza a conversão: 1 km = 1000 metros
const resultadoEmMetros=valorEmKm * 1000;

setMetros(resultadoEmMetros);
};

return (
<View style={styles.container}>
<Text style={styles.title}>Conversor de Unidades
</Text>
<Text style={styles.subtitle}>Quilômetros para
Metros</Text>

<View style={styles.inputContainer}>
<TextInput
style={styles.input}
placeholder="Digite o valor em km"
keyboardType="numeric" // Mostra o teclado numérico
value={km}
onChangeText={text => setKm(text)}
/>
</View>

<TouchableOpacity style={styles.button} onPress
={handleConvert}>
<Text style={styles.buttonText}>Converter</Text>
</TouchableOpacity>

{metros !== null && (
<View style={styles.resultContainer}>
<Text style={styles.resultText}>
{km} km equivalem a:
</Text>
<Text style={styles.resultValue}>
{metros} metros
</Text>
</View>
)}
</View>
);
}

const styles = StyleSheet.create({
container: {
flex: 1,
backgroundColor: '#f0f4f7',
alignItems: 'center',
justifyContent: 'center',
padding: 20,
},
title: {
fontSize: 28,
fontWeight: 'bold',
marginBottom: 10,
color: '#333',
},
subtitle: {
fontSize: 18,
marginBottom: 30,
color: '#555',
},
inputContainer: {
width: '100%',
marginBottom: 20,
},
input: {
height: 50,
borderColor: '#ccc',
borderWidth: 1,
borderRadius: 8,
paddingHorizontal: 15,
fontSize: 18,
backgroundColor: '#fff',
shadowColor: '#000',
shadowOffset: { width: 0, height: 2 },
shadowOpacity: 0.1,
shadowRadius: 2,
elevation: 2,
},
button: {
backgroundColor: '#007bff',
paddingVertical: 15,
paddingHorizontal: 40,
borderRadius: 8,
shadowColor: '#000',
shadowOffset: { width: 0, height: 2 },
shadowOpacity: 0.2,
shadowRadius: 2,
elevation: 3,
},
buttonText: {
color: '#fff',
fontSize: 18,
fontWeight: 'bold',
},
resultContainer: {
marginTop: 30,
alignItems: 'center',
padding: 20,
backgroundColor: '#e9ecef',
borderRadius: 10,
borderWidth: 1,
borderColor: '#dee2e6',
width: '100%',
},
resultText: {
fontSize: 20,
color: '#495057',
},
resultValue: {
fontSize: 26,
fontWeight: 'bold',
marginTop: 10,
color: '#28a745',
},
});