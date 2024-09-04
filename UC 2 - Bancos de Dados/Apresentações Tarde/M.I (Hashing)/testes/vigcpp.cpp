#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Função para alinhar a chave com o tamanho da mensagem
string alligner(const string& chave, const string& mensagem) {
    string chaveExtendida = chave;
    while (chaveExtendida.length() < mensagem.length()) {
        chaveExtendida += chave;
    }
    return chaveExtendida.substr(0, mensagem.length());
}

int main() {
    const string alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    // Entrada da mensagem e chave
    string msg, chave;
    cout << "Insira a Mensagem: ";
    getline(cin, msg);
    cout << "Insira a chave: ";
    getline(cin, chave);
    
    // Convertendo para maiúsculas
    transform(msg.begin(), msg.end(), msg.begin(), ::toupper);
    transform(chave.begin(), chave.end(), chave.begin(), ::toupper);
    
    // Valores numéricos da mensagem e chave
    vector<int> nmsg, nkey, ncifra;
    string cifra;
    
    // Chave estendida
    string keyout = alligner(chave, msg);
    
    // Imprimindo a mensagem e a chave
    cout << "\n       Mensagem        |      Chave\n";
    for (size_t i = 0; i < msg.length(); ++i) {
        char charM = msg[i];
        char charK = keyout[i];
        int posM = alfabeto.find(charM);
        int posK = alfabeto.find(charK);
        cout << charM << "------------------->" << (posM < 10 ? "0" : "") << posM << " | " 
             << charK << "------------------->" << (posK < 10 ? "0" : "") << posK << endl;
        nmsg.push_back(posM);
        nkey.push_back(posK);
    }
    
    // Cifra da mensagem
    for (size_t i = 0; i < nmsg.size(); ++i) {
        int cifraPos = (nmsg[i] + nkey[i]) % 26;
        ncifra.push_back(cifraPos);
        cifra += alfabeto[cifraPos];
    }
    
    // Exibindo resultados
    cout << "\n" << msg << "\n\n";
    cout << "Valor Numérico da Mensagem\n";
    for (int num : nmsg) cout << num << " ";
    cout << "\n\nValor Numérico da Chave após alinhamento:\n";
    for (int num : nkey) cout << num << " ";
    cout << "\n\nAlinhamento de chave: " << keyout << "\n\n";
    cout << "Mensagem Cifrada:\n";
    for (int num : ncifra) cout << num << " ";
    cout << "\n" << cifra << endl;

    return 0;
}
