#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Função para alinhar a chave com o tamanho da mensagem
void alligner(const char* chave, const char* mensagem, char* chaveExtendida) {
    size_t chaveLen = strlen(chave);
    size_t msgLen = strlen(mensagem);
    size_t i, j = 0;

    for (i = 0; i < msgLen; ++i) {
        chaveExtendida[i] = chave[j];
        j = (j + 1) % chaveLen;
    }
    chaveExtendida[msgLen] = '\0';  // Adiciona o terminador nulo ao final da string
}

int main() {
    char msg[256], chave[256], chaveExtendida[256];
    const char alfabeto[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int nmsg[256], nkey[256], ncifra[256];
    char cifra[256];
    size_t i, msgLen;

    // Entrada da mensagem e chave
    printf("Insira a Mensagem: ");
    fgets(msg, sizeof(msg), stdin);
    msg[strcspn(msg, "\n")] = '\0';  // Remove o caractere de nova linha, se presente
    printf("Insira a chave: ");
    fgets(chave, sizeof(chave), stdin);
    chave[strcspn(chave, "\n")] = '\0';  // Remove o caractere de nova linha, se presente

    // Convertendo para maiúsculas
    for (i = 0; msg[i]; ++i) msg[i] = toupper((unsigned char)msg[i]);
    for (i = 0; chave[i]; ++i) chave[i] = toupper((unsigned char)chave[i]);

    // Alinhamento da chave
    msgLen = strlen(msg);
    alligner(chave, msg, chaveExtendida);

    // Imprimindo a mensagem e a chave
    printf("\n       Mensagem        |      Chave\n");
    for (i = 0; i < msgLen; ++i) {
        char charM = msg[i];
        char charK = chaveExtendida[i];
        int posM = strchr(alfabeto, charM) - alfabeto;
        int posK = strchr(alfabeto, charK) - alfabeto;
        printf("%c------------------->%02d | %c------------------->%02d\n", charM, posM, charK, posK);
        nmsg[i] = posM;
        nkey[i] = posK;
    }

    // Cifra da mensagem
    for (i = 0; i < msgLen; ++i) {
        int cifraPos = (nmsg[i] + nkey[i]) % 26;
        ncifra[i] = cifraPos;
        cifra[i] = alfabeto[cifraPos];
    }
    cifra[msgLen] = '\0';  // Adiciona o terminador nulo ao final da string

    // Exibindo resultados
    printf("\n%s\n\n", msg);
    printf("Valor Numérico da Mensagem\n");
    for (i = 0; i < msgLen; ++i) printf("%d ", nmsg[i]);
    printf("\n\nValor Numérico da Chave após alinhamento:\n");
    for (i = 0; i < msgLen; ++i) printf("%d ", nkey[i]);
    printf("\n\nAlinhamento de chave: %s\n\n", chaveExtendida);
    printf("Mensagem Cifrada:\n");
    for (i = 0; i < msgLen; ++i) printf("%d ", ncifra[i]);
    printf("\n%s\n", cifra);

    return 0;
}
